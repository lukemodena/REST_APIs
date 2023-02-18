import json

year = "YE"+input_data['dealname'].rsplit(' ', 1)[1]

Description = "Associate Fee for R&D Tax relief claim: \n- Rate "+input_data['COP']+" \n- "+year+": Fee "+input_data['CF']

if 'COF' in input_data:
    if input_data['COF'] is None:
        Rate = 0.0
    else:
        Rate = float(input_data['COF'])
else:
    Rate = 0.0
       
VATAmount = Rate*0.2


my_data = '''
{
    "Category": {
            "Number": 1,
            "IconType": "flag",
            "IconId": 2,
            "Name": "2 Sent To Tax Accountant",
            "IconColor": "blue"
    },
    "Currency": {
        "Code": "GBP",
        "ExchangeRate": 50.0000,
        "Name": "British Pounds",
        "Symbol": "£",
        "DisplaySymbolOnRight": false
    },
    "CurrencyName": null,
    "CustomerCode": input_data['CustomerCode'],
    "CustomerDiscount": 0.0000,
    "CustomerName": input_data['CustomerName'],
    "Date": input_data['Date'],
    "DefaultChargeType": 9998,
    "Ec": 0,
    "GrossAmount": 120.0000,
    "LineItems": [{
        "NominalCode": 4906,
        "Description": "",
        "ProductCode": "ANNU0001",
        "Quantity": 1.0000,
        "HomeCurrencyRate": 10.0000,
        "HomeCurrencyVATAmount": 20.0000,
        "VATExempt": false,
        "VATLevel": 20.0000,
        "TaxCode": "",
        "Rate":730.77,
        "VATAmount":146.15
    }],
    "NetAmount": 100.0000,
    "NextNumber": 0,
    "Number": 0,
    "OutSideEc": 0,
    "PreviousNumber": 0,
    "ProjectNumber": 0,
    "CustomerReference": "",
    "SuppressAmount": 0,
    "VATAmount": 20.0000,
    "VATNumber": ""
}
'''
x = json.loads(my_data)
x['Category']['Number'] = int(input_data['catNo'])
x['Category']['IconType'] = "flag"
x['Category']['IconId'] = int(input_data['catIcon'])
x['Category']['Name'] = input_data['catName']
x['Category']['IconColor'] = input_data['catColour']
x['Date'] = input_data['date']
x['NextNumber'] = int(input_data['nextNo'])
x['Number'] = int(input_data['quoteno'])
x['PreviousNumber'] = int(input_data['prevNo'])
x['CustomerReference'] = input_data['dealname']
x['ProjectNumber'] = int(input_data['projNo'])
x['LineItems'][0]['Rate'] = Rate
x['LineItems'][0]['Description'] = Description
x['LineItems'][0]['VATAmount'] = VATAmount

y = json.dumps(x, indent=4)
my_headers = {
    'Accept' : 'application/json',
    'Content-Type' : 'application/json',
    'Authorization' : input_data['token'],
    'Connection': 'keep-alive',
    'Origin' : 'chrome-extension: //rest-console-id',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22'
}

response = requests.put(f'https://api.kashflow.com/v2/quotes/{input_data['QuoteID']}', headers=my_headers, data = y)

output = response.json()
