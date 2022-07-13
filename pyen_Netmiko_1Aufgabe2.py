from netmiko import ConnectHandler
from getpass import getpass

devices = [{'ip': '192.168.181.21',
            'device_type': 'cisco_nxos'},
           {'ip': '192.168.181.22',
            'device_type': 'cisco_nxos'},
           {'ip': '192.168.181.23',
            'device_type': 'cisco_nxos'},
           {'ip': '192.168.181.24',
            'device_type': 'cisco_nxos'}
           ]

user = input('Username: ')
passw = getpass()

for device in devices:
    host = device['ip']
    with ConnectHandler(username=user, password=passw, **device) as net_connect:
        print(f'Connected to {host}')
        show = 'show inventory'
        cmd = net_connect.send_command(show)
        print(cmd)

print('**************************************************************')