from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from devices import devices
from concurrent.futures import ThreadPoolExecutor, as_completed
from logging_automation import setup_logging, log_message # Logging
import os

# Defining the device's information

# username = "vagrant"
# #password = getpass()
# password = os.getenv('NETMIKO_PASSWORD')

# Set up logging
logger = setup_logging()

# Command to be executed
command = "show ip int brief"

# Function to execute the command on a device
def execute_command(device, command):
    try:
        log_message(logger, f"Connecting to device {device['ip']}")
        with ConnectHandler(**device) as net_connect:
            output = net_connect.send_command(command, use_textfsm=True)
            log_message(logger, f"Command executed on device {device['ip']}")
            return {device['ip']: output}
    except Exception as e:
        log_message(logger, f"Error executing command on device {device['ip']}: {e}")
        raise

# Main function to run tasks in parallel
def main():
    log_message(logger, "Starting script execution")
    with ThreadPoolExecutor(max_workers=len(devices)) as executor:
        future_to_device = {executor.submit(execute_command, device, command): device for device in devices}
        
        for future in as_completed(future_to_device):
            device = future_to_device[future]
            try:
                result = future.result()
                log_message(logger, f"Received output from device {device['ip']}")
                print(f"Output from device {device['ip']}:\n")
                pprint(result)
                print()
            except Exception as exc:
                log_message(logger, f"Device {device['ip']} generated an exception: {exc}")
                print(f"Device {device['ip']} generated an exception: {exc}")

    log_message(logger, "Script execution completed")

if __name__ == "__main__":
    main()




# # Version without logging setup


# from netmiko import ConnectHandler
# from getpass import getpass
# from pprint import pprint
# from devices import devices
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import os

# # Defining the device's information

# # username = "vagrant"
# # #password = getpass()
# # password = os.getenv('NETMIKO_PASSWORD')

# # Set up logging
# logger = setup_logging()


# # Command to be executed
# command = "show ip int brief"

# # Function to execute the command on a device
# def execute_command(device, command):
#     with ConnectHandler(**device) as net_connect:
#         output = net_connect.send_command(command, use_textfsm=True)
#         return {device['ip']: output}

# # Main function to run tasks in parallel
# def main():
#     with ThreadPoolExecutor(max_workers=len(devices)) as executor:
#         future_to_device = {executor.submit(execute_command, device, command): device for device in devices}
        
#         for future in as_completed(future_to_device):
#             device = future_to_device[future]
#             try:
#                 result = future.result()
#                 print(f"Output from device {device['ip']}:\n")
#                 pprint(result)
#                 print()
#             except Exception as exc:
#                 print(f"Device {device['ip']} generated an exception: {exc}")

# if __name__ == "__main__":
#     main()

