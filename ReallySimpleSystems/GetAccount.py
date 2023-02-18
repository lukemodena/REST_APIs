import requests
from requests.structures import CaseInsensitiveDict
import json

compName = input_data['compName']

url = "https://apiv4.reallysimplesystems.com/accounts"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer {}".format(input_data['token'])

resp = requests.get(url, headers=headers)
data = resp.json()

return data
