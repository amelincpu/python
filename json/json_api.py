import requests
import json
import os
import sys

print('\n', '*'*50, '\n', end='')
git_api_response = requests.get('https://api.github.com', headers={'Authorization': 'access_token 11111111111111111111111'})
git_api_response_text = json.loads(git_api_response.text)
print(json.dumps(git_api_response_text, indent=4))
with open(os.path.join(sys.path[0], 'git_api_response.json'), 'w') as git_api_response_file:
    json.dump(git_api_response_text, git_api_response_file, indent=4)    

print('\n', '*'*50, '\n', end='')