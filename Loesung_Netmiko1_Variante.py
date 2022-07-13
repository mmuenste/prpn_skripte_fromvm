from time import strftime
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

username = input('Username: ')
passw = getpass()

for dev in devices:
    with ConnectHandler(username=username, password=passw,**dev) as net_connect:
        host = dev['ip']
        print(host, '... connected')
        config = net_connect.send_command('show run')
        # print(config)
        filename = host.replace(".", "_") + '_' + strftime("%Y%m%d_%H%M%S") + '.config'
        with open(filename, 'w') as cfg_file:
            cfg_file.write(config)
