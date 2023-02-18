import requests
from requests.structures import CaseInsensitiveDict
import json

url = "https://apiv4.reallysimplesystems.com/accounts/{}".format(input_data['accountId'])

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer {}".format(input_data['token'])

postNewData = {
    "name": input_data['name'],
    "addressline": input_data['addressline'],
    "addresscity": input_data['addresscity'],
    "addresspostcode/zip": input_data['addresspostcode'],
    "website": input_data['website'],
    "phone": input_data['phone']
}

resp = requests.patch(url, headers=headers, data=postNewData)

return resp.json()
