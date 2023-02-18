import json

my_headers = {
    'Accept' : 'application/json',
    'Content-Type' : 'application/json',
    'Authorization' : input_data['token'],
    'Connection': 'keep-alive',
    'Origin' : 'chrome-extension: //rest-console-id',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22'
}
response = requests.get(input_data['API'], headers=my_headers)

## Does Part-Payment Exist? ##

try:
    x = response.json()["LineItems"][1]["Description"]
    PartpaymentExists = True
    output = [{"Part-payment Exists": PartpaymentExists, "Description1": response.json()["LineItems"][0]["Description"], "Rate1": response.json()["LineItems"][0]["Rate"], "VATAmount1": response.json()["LineItems"][0]["VATAmount"], "Number1": response.json()["LineItems"][0]["Number"], "Description2": response.json()["LineItems"][1]["Description"], "Rate2": response.json()["LineItems"][1]["Rate"], "VATAmount2": response.json()["LineItems"][1]["VATAmount"], "Number2": response.json()["LineItems"][1]["Number"]}]
    return output

except:
    PartpaymentExists = False
    output = [{"Part-payment Exists": PartpaymentExists, "Description1": response.json()["LineItems"][0]["Description"], "Rate1": response.json()["LineItems"][0]["Rate"], "VATAmount1": response.json()["LineItems"][0]["VATAmount"], "Number1": response.json()["LineItems"][0]["Number"]}]
    return output
