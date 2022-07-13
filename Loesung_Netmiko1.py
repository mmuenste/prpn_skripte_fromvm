from time import time
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
    net_connect = ConnectHandler(username=username, password=passw,**dev)
    host = dev['ip']
    print(host, '... connected')
    config = net_connect.send_command('show run')
    # print(config)
    filename = host.replace(".", "_") + '_' + str(time()) + '.config'
    cfg_file = open(filename, 'w')
    for line in config:
        cfg_file.write(line)
    cfg_file.close()
    net_connect.disconnect()
