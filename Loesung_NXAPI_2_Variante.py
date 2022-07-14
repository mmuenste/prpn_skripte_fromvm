import requests
from lxml import etree

URL = "http://192.168.181.21/ins"
CRED = ("admin", "cisco")

COMMAND = """<?xml version="1.0"?>
<ins_api>
  <version>1.0</version>
  <type>cli_show</type>
  <chunk>0</chunk>
  <sid>sid</sid>
  <input>sho int br</input>
  <output_format>xml</output_format>
</ins_api>"""

HDR = {'Content-type': 'application/xml',
       'Accept': 'application/xml'}

RESP = requests.post(URL, headers=HDR, auth=CRED, data=COMMAND)

RESP_PAYLOAD = RESP.text
print(RESP.status_code)
print(RESP.text)
print(type(RESP_PAYLOAD))
TREE = etree.fromstring(RESP_PAYLOAD)
print('List of Vlans for Access interfaces:')

for i in TREE.iter('ROW_interface'):
    interface = i.find('interface')
    pmode = i.find('portmode')
    vlan = i.find('vlan')
    try:
      if pmode.text == 'access':
          print("Access-Interface {}\t\tVlans: {}".format(interface.text,
                                                          vlan.text))
      if pmode.text == 'trunk':
          print("Trunk-Interface {}\t\tVlan: {}".format(interface.text,
                                                        vlan.text))
    except AttributeError:
      continue

