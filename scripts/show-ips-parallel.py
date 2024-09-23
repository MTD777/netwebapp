from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from devices import devices
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

# Defining the device's information

# username = "vagrant"
# #password = getpass()
# password = os.getenv('NETMIKO_PASSWORD')


# Command to be executed
command = "show ip int brief"

# Function to execute the command on a device
def execute_command(device, command):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command(command, use_textfsm=True)
        return {device['ip']: output}

# Main function to run tasks in parallel
def main():
    with ThreadPoolExecutor(max_workers=len(devices)) as executor:
        future_to_device = {executor.submit(execute_command, device, command): device for device in devices}
        
        for future in as_completed(future_to_device):
            device = future_to_device[future]
            try:
                result = future.result()
                print(f"Output from device {device['ip']}:\n")
                pprint(result)
                print()
            except Exception as exc:
                print(f"Device {device['ip']} generated an exception: {exc}")

if __name__ == "__main__":
    main()

