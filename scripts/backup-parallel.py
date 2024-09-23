import os
from datetime import datetime
from netmiko import ConnectHandler
from devices import devices  # Import the device information
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define the custom folder path for backups
backup_folder = 'backup-files/'

# Ensure the backup folder exists
os.makedirs(backup_folder, exist_ok=True)

# Backup device configurations and save them locally
def backup_config(device):
    try:
        connection = ConnectHandler(**device)
        connection.enable()
        
        # Get running configuration
        running_config = connection.send_command("show running-config")

        # Get the current date and format it
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Define file path including the custom folder and date
        file_path = os.path.join(backup_folder, f"{device['ip']}_backup_{current_date}.txt")
        
        # Save config to a file
        with open(file_path, 'w') as f:
            f.write(running_config)
        
        print(f"Backup for {device['ip']} successful.")
        connection.disconnect()
    
    except Exception as e:
        print(f"Error backing up {device['ip']}: {e}")

# Main function to run backups in parallel
def main():
    with ThreadPoolExecutor(max_workers=len(devices)) as executor:
        future_to_device = {executor.submit(backup_config, device): device for device in devices}
        
        for future in as_completed(future_to_device):
            device = future_to_device[future]
            try:
                future.result()
            except Exception as exc:
                print(f"Device {device['ip']} generated an exception: {exc}")

if __name__ == "__main__":
    main()
