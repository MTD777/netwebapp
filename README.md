# Netmiko Script Runner with Django Integration

This is a GitHub project which deploys a Netmiko Script runner integrated with the Django framework, used as a Web app GUI.

## Purpose

The purpose of this project is to extend and improve knowledge of network automation and software development principles. By integrating Netmiko with Django, this project aims to provide a user-friendly interface for running network automation scripts, making it easier to manage and automate network tasks.

## Instructions - High level steps

- Copy the project to your local PC using git clone. (git clone <project_name>)
- Access the folder. (cd netwebapp)
- Create a .env file and add the variables for NETMIKO_USERNAME NETMIKO_PASSWORD
- Install docker compose.
- Initialize the app with docker compose (docker compose up / or / docker compose up -d --build).
- Access the application from your browser (http://<your_server_IP_address:8000>).
- Run scripts! 

### How to set up your environment?

- Navigate to scripts/devices.py
- Adapt the device's dictionary to match your lab environment

### How to add new scripts?

- Add your netmiko scripts under scripts/
- Add a new button for each new script in the HTML file, script_runner/templates/script_runner

## Upcoming Features

- **User Authentication**: Implementing user login and registration to secure access to the application.
- **Script Scheduling**: Adding the ability to schedule scripts to run at specified times.
- **Enhanced Logging**: Improving logging capabilities to provide detailed execution logs and error reports.
- **Multi-Device Support**: Extending support to run scripts on multiple devices simultaneously.
- **UI Enhancements**: Improving the user interface for a more intuitive and seamless experience.
- **Encryption**: Encrypting sensitive values/files.
- **Intergration with Reverse Proxy/HTTPs**: For secure transport access using HTTPs.

Stay tuned for these exciting updates!



