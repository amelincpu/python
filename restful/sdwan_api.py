import json
import requests
from requests import api

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ip = 'sandbox-sdwan-1.cisco.com'
user = 'devnetuser'
passw = 'RG!_Yw919_83'

apiurl = 'https://{}'.format(ip)

logact = 'j_security_check'
logdata = {
    "j_username": "devnetuser",
    "j_password": "RG!_Yw919_83",
    }

logurl = apiurl + logact

sess = requests.session()
logresp = sess.post(url=logurl, data=json.dumps(logdata), verify=False)

devres = 'dataservice/device'
devurl = apiurl + devres

devresp = sess.get(devurl, verify=False)
devitems = json.loads(devresp.content)['data']

for item in devitems:
    print(item['device-model'])
