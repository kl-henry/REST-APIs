import json

import requests

# ---- Simple REST API Aufruf
# response = requests.get("http://api.open-notify.org/astros.json")
# print(response)

#print(response.content()) # Return the raw bytes of the data payload
#print(response.text()) # Return a string representation of the data payload
# print(response.json()) # This method is convenient when the API returns JSON

# ----  REST API Aufruf mit Parametern
# query = {'lat':'45', 'lon':'180'}
# response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
# print(response.json())

# ----  REST API Aufruf mit Authentizierung
# from requests.auth import HTTPBasicAuth
#
# response = requests.get(
#   'https://api.github.com/user',
#   auth=HTTPBasicAuth('kl-henry', 'Dec2Ute3')
# )
# print(response.json())


username = 'user'
token = 'token'
login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))

# Example 2 (headers):
headers = {'Authorization': 'token ' + token}
login = requests.get('https://api.github.com/user', headers=headers)
print(login.json())



# Example 3 (delete repo):
user = 'username'
repo = 'some_repo' # Delete this repo
headers = {'Authorization': 'token ' + token}
login = requests.delete('https://api.github.com/' + 'repos/' + user + '/' + repo, headers=headers)


# Example 4 (create repo):
repo = 'some_repo'
description = 'Created with api'
payload = {'name': repo, 'description': description, 'auto_init': 'true'}
login = requests.post('https://api.github.com/' + 'user/repos', auth=(user,token), data=json.dumps(payload))

try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)