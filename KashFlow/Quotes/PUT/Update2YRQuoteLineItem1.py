import json
from datetime import date, datetime

# First CY
year1 = input_data['YE1']
Description1 = "Associate Fee for R&D Tax relief claim: \n- Rate "+input_data['COP1']+" \n- "+year1+": Fee "+input_data['CF1']

if 'COF1' in input_data:
    if input_data['COF1'] is None:
        Rate1 = 0.0
    else:
        Rate1 = float(input_data['COF1'])
else:
    Rate1 = 0.0
       
VATAmount1 = Rate1*0.2

# Second CY

Description2 = input_data['Description2']
Rate2 = float(input_data['Rate2'])      
VATAmount2 = float(input_data['VATAmount2'])

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
today = now.strftime("%Y-%m-%d %H:%M:%S +00:00")

QuoteNo = int(input_data['quotenumber'])
    
my_data = '''
{
    "Category": {
            "Number": 1,
            "IconType": "flag",
            "IconId": 1,
            "Name": "1 Provisional Figures",
            "IconColor": "purple"
    },
    "Currency": {
        "Code": "GBP",
        "ExchangeRate": 50.0000,
        "Name": "British Pounds",
        "Symbol": "£",
        "DisplaySymbolOnRight": false
    },
    "CurrencyName": null,
    "CustomerCode": COMPANY_CODE,
    "CustomerDiscount": 0.0000,
    "CustomerName": "COMPANY_NAME",
    "Date": "",
    "DefaultChargeType": 9998,
    "Ec": 0,
    "GrossAmount": 120.0000,
    "LineItems": [{
        "NominalCode": 4906,
        "Description": "",
        "ProductCode": "ANNU0001",
        "Quantity": 1,
        "HomeCurrencyRate": 10.0000,
        "HomeCurrencyVATAmount": 20.0000,
        "Number": 0,
        "VATExempt": false,
        "VATLevel": 20.0000,
        "TaxCode": "",
        "Rate":0,
        "VATAmount": 0
    }, {
        "NominalCode": 4906,
        "Description": "",
        "ProductCode": "ANNU0003",
        "Quantity": 1,
        "HomeCurrencyRate": 10.0000,
        "HomeCurrencyVATAmount": 20.0000,
        "Number": 0,
        "VATExempt": false,
        "VATLevel": 20.0000,
        "TaxCode": "",
        "Rate":0,
        "VATAmount": 0
    }],
    "NetAmount": 100.0000,
    "NextNumber": 0,
    "Number": "",
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
x['Category']['Number'] = input_data['CategoryNo']
x['Category']['Name'] = input_data['CategoryName']
x['Category']['IconColor'] = input_data['CategoryColour']
x['Category']['IconId'] = input_data['CategoryID']
#x['Date'] = today
x['Date'] = input_data['Date']
x['NextNumber'] = QuoteNo + 1
x['Number'] = QuoteNo
x['PreviousNumber'] = QuoteNo - 1
x['CustomerReference'] = input_data['QuoteName']
x['ProjectNumber'] = int(input_data['projectno'])
x['LineItems'][0]['Rate'] = Rate1
x['LineItems'][0]['Description'] = Description1
x['LineItems'][0]['VATAmount'] = VATAmount1
x['LineItems'][1]['Rate'] = Rate2
x['LineItems'][1]['Description'] = Description2
x['LineItems'][1]['VATAmount'] = VATAmount2

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
