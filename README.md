# Automation-Script

Python script for basic network automation using GNS3 and Cisco IOS devices.  
This project automates switch configuration tasks such as VLAN creation, hostname setup, MOTD banner configuration, trunk port setup, and access port assignment.

## Features

- Configure switch hostname
- Set MOTD banner
- Create VLANs
- Assign VLAN names
- Configure trunk ports
- Configure access ports
- Connect to Cisco IOS devices using Netmiko

## Technologies Used

- Python
- Netmiko
- GNS3
- Cisco IOS

## Lab Environment

This project was tested in a local lab environment using GNS3 with Cisco IOS switches and a cloud/NAT connection.

## Requirements

Install the required library before running the script:

```bash
pip install netmiko

How to Run
	1.	Open the terminal
	2.	Navigate to the project folder
	3.	Run the script:
python Switch.py
Enter the required inputs when prompted:
	•	username
	•	password
	•	enable password
	•	hostname
	•	MOTD
	•	VLAN ID
	•	VLAN name
	•	trunk port
	•	access port
