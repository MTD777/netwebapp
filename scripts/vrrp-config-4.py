from netmiko import ConnectHandler
from devices import devices  # Import the list of devices
from logging_automation import setup_logging, log_message
from retry_logic import retry


# Version 4 adding retry logic as function/module - more reusable

# Set up logging
logger = setup_logging()

# Filter devices with 'arista_eos' device type
arista_devices = [device for device in devices if device['device_type'] == 'arista_eos']

# Initialize variables
hostnames = {}
vlan_ids = {}
vrrp_addresses = {}

def connect_and_gather_info(device):
    def task():
        net_connect = ConnectHandler(**device)
        log_message(logger, f"Connected to {device['ip']}")
        
        # Get hostname
        hostname = net_connect.send_command('show hostname').strip()
        hostnames[hostname] = device
        log_message(logger, f"Retrieved hostname: {hostname}")
        
        # Get VLAN ID from 'show ip int br'
        ip_int_br = net_connect.send_command('show ip int br')
        vlan_id = None
        for line in ip_int_br.splitlines():
            if 'Vlan' in line:
                vlan_id = line.split()[0].replace('Vlan', '')
                vlan_ids[hostname] = vlan_id
                log_message(logger, f"Retrieved VLAN ID: {vlan_id} for hostname: {hostname}")
                break
        
        # Get VRRP address from 'show run'
        show_run = net_connect.send_command('show run')
        vrrp_address = None
        for line in show_run.splitlines():
            if 'ip virtual-router address' in line:
                vrrp_address = line.split()[-1]
                break
        vrrp_addresses[hostname] = vrrp_address
        log_message(logger, f"Retrieved VRRP address: {vrrp_address} for hostname: {hostname}")
        
        net_connect.disconnect()
        log_message(logger, f"Disconnected from {device['ip']}")
        return True
    
    return retry(task, logger)

# Connect to each device and gather required information
for device in arista_devices:
    if not connect_and_gather_info(device):
        log_message(logger, f"Failed to process device {device['ip']} after 3 attempts")

# Determine IP and VRRP priority based on hostname
sorted_hostnames = sorted(hostnames.keys())
lower_ip_suffix = '2'
higher_ip_suffix = '3'
lower_priority = 110
higher_priority = 100

def configure_device(device, hostname, ip_address, priority, vlan_id):
    def task():
        net_connect = ConnectHandler(**device)
        log_message(logger, f"Connected to {device['ip']} for configuration")
        
        config_commands = [
            f'int vlan {vlan_id}',
            f'ip address {ip_address}/24',
            f'vrrp 1 priority-level {priority}'
        ]
        
        net_connect.send_config_set(config_commands)
        log_message(logger, f"Configured {hostname} with IP {ip_address} and VRRP priority {priority}")
        
        net_connect.disconnect()
        log_message(logger, f"Disconnected from {device['ip']} after configuration")
        return True
    
    return retry(task, logger)

# Configure devices
for i, hostname in enumerate(sorted_hostnames):
    device = hostnames[hostname]
    base_ip = vrrp_addresses[hostname].rsplit('.', 1)[0]
    ip_address = f"{base_ip}.{lower_ip_suffix}" if i % 2 == 0 else f"{base_ip}.{higher_ip_suffix}"
    priority = lower_priority if i % 2 == 0 else higher_priority
    vlan_id = vlan_ids[hostname]
    
    if not configure_device(device, hostname, ip_address, priority, vlan_id):
        log_message(logger, f"Failed to configure device {device['ip']} after 3 attempts")
