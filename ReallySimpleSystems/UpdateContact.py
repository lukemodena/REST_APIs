import requests
from requests.structures import CaseInsensitiveDict
import json

url = "https://apiv4.reallysimplesystems.com/contacts/{}".format(input_data['contactId'])

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer {}".format(input_data['token'])

postNewData = {
    "salutation": input_data['salutation'],
    "first": input_data['first'],
    "last": input_data['last'],
    "email": input_data['email'],
    "phone": input_data['phone']
}

resp = requests.patch(url, headers=headers, data=postNewData)

return resp.json()
