# devices.py

import os
from netmiko import ConnectHandler

username = os.getenv('NETMIKO_USERNAME')
password = os.getenv('NETMIKO_PASSWORD')

# Make sure to set the variables 

# export NETMIKO_USERNAME='your_username'
# export NETMIKO_PASSWORD='your_password'


# Device information: store IPs, credentials, and other necessary details.
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
