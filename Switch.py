from netmiko import ConnectHandler
import getpass

HOST = "192.168.201.100"
username = input("Username: ")
password = getpass.getpass("Password: ")
enable_pass = getpass.getpass("Enable Password: ")
new_hostname = input("New Hostname: ")
motd_msg = input("MOTD Message: ")

vlan_id = input("VLAN ID: ")
vlan_name = input("VLAN Name: ")
trunk_port = input("Trunk Port: ")

device = {
    'device_type': 'cisco_ios_telnet',
    'host': HOST,
    'username': username,
    'password': password,
    'secret': enable_pass,
    'port': 23,
    'timeout': 10
}

try:
    print(f"\n{'='*50}")
    print(f"Connecting to {HOST}...")
    print(f"{'='*50}\n")

    connection = ConnectHandler(**device)
    connection.enable()

    print("Applying Basic Configuration...")
    basic_config = [
        f'hostname {new_hostname}',
        f'banner motd |{motd_msg}|',
        'service password-encryption',
        'no ip domain-lookup',
        'line console 0',
        ' logging synchronous',
        ' exec-timeout 0 0',
        'line vty 0 4',
        ' logging synchronous',
        ' transport input telnet',
        ' exit'
    ]
    output = connection.send_config_set(basic_config)
    print(output)

    connection.set_base_prompt()

    print(f"\nCreating VLAN {vlan_id}...")
    vlan_config = [
        f'vlan {vlan_id}',
        f'name {vlan_name}',
        'exit'
    ]
    output = connection.send_config_set(vlan_config)
    print(output)

    print(f"\nConfiguring Trunk Port {trunk_port}...")
    trunk_config = [
        f'interface {trunk_port}',
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        f'switchport trunk allowed vlan {vlan_id}',
        'no shutdown',
        'exit'
    ]
    output = connection.send_config_set(trunk_config)
    print(output)

    print("\nSaving configuration...")
    connection.save_config()
    print("Configuration saved successfully!")

    print("\n" + "=" * 50)
    print("Verification Commands:")
    print("=" * 50)

    print("\nVLAN Information:")
    print(connection.send_command("show vlan brief"))

    print("\nTrunk Information:")
    print(connection.send_command("show interfaces trunk"))

    print("\nInterface Status:")
    print(connection.send_command("show ip interface brief"))

    print("\nRunning Config:")
    print(connection.send_command("show running-config"))

    connection.disconnect()
    print("\nAll done! Disconnected.")

except Exception as e:
    print(f"\nError: {e}")