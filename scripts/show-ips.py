from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
import os

# Defining the device's information

username = "vagrant"
#password = getpass()
password = os.getenv('NETMIKO_PASSWORD')

devices = [
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.121.102',
        'username': username,
        'password': password,
        'secret': password,  # Enable password if required
    },
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.121.103',
        'username': username,
        'password': password,
        'secret': password,  
    },
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.121.106',
        'username': username,
        'password': password,
        'secret': password,  
    },
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.121.107',
        'username': username,
        'password': password,
        'secret': password,  
    },
    {
        'device_type': 'arista_eos',
        'ip': '192.168.121.108',
        'username': username,
        'password': password,
        'secret': password,
    },
    {
        'device_type': 'arista_eos',
        'ip': '192.168.121.109',
        'username': username,
        'password': password,
        'secret': password,
    },
    {
        'device_type': 'arista_eos',
        'ip': '192.168.121.110',
        'username': username,
        'password': password,
        'secret': password,
    },
    {
        'device_type': 'arista_eos',
        'ip': '192.168.121.111',
        'username': username,
        'password': password,
        'secret': password,
    }
]



# Connecting to the devices and retrieving the output

command = "show ip int brief"

for device in devices:
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command(command, use_textfsm=True)
        
        print(f"Output from device {device['ip']}:\n")
        pprint(output)
        print()

# How it was

# command = "show ip int brief"
# with ConnectHandler(**cisco1) as net_connect:
#     # Use TextFSM to retrieve structured data
#     output = net_connect.send_command(command, use_textfsm=True)


# print()
# pprint(output)
# print()