from dnacentersdk import api

dnac = api.DNACenterAPI(username='devnetuser',
                        password='Cisco123!',
                        base_url='https://sandboxdnac2.cisco.com')

listdevices = dnac.devices.get_device_list()

print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format(' Device Name', '|', ' Device Type', '|', ' Up Time'), '\n', '-'*95)

for device in listdevices.response:
    print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format(str(device.hostname), '|', str(device.type), '|', str(device.upTime)))
