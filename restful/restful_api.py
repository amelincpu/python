import requests
import json

url = 'http://worldclockapi.com/api/json/gmt/now'
api_out = requests.request('GET', url)
api_out_dic = json.loads(api_out.text)
print('\nCurrent time is: ', api_out_dic['currentDateTime'], '\n')