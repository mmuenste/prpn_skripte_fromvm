import requests

headers = {"Accept": "application/yang-data+json"}

url = r"https://192.168.181.11/restconf/data/openconfig-interfaces:interfaces/interface=eth1%2F100"

rest = requests.get(url, auth=("cisco", "cisco"), headers=headers,  verify=False)

print(rest.text)