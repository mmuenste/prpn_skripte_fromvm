import requests

#import json

IP = "192.168.181.22"
TOKEN_URL = f"http://{IP}/api/aaaLogin.json"

TOKEN_PAYLOAD = {
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "cisco"
}}}

#TOKEN_ANFORDERN = requests.post(TOKEN_URL, data=json.dumps(TOKEN_PAYLOAD))
TOKEN_ANFORDERN = requests.post(TOKEN_URL, json=TOKEN_PAYLOAD)
print(TOKEN_ANFORDERN.json())
print("*" * 30)
print()

cookie = TOKEN_ANFORDERN.cookies
print(cookie)
print("*" * 30)
print()

# Vlan anlegen

VLAN_URL = f"http://{IP}/api/mo/sys/bd.json"

VLAN_PAYLOAD = {
"bdEntity": {
  "children": [
    {
      "l2BD": {
        "attributes": {
          "fabEncap": "vlan-25",
          "pcTag": "1"
}}}]}}  

create_vlan = requests.post(VLAN_URL, json=VLAN_PAYLOAD, cookies=cookie)

print(create_vlan.json())
print(create_vlan.status_code)
print("*" * 30, end="\n\n")




