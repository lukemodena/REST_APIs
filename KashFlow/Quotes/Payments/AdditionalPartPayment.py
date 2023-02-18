import json
from datetime import date, datetime

# First CY

Description1 = input_data['Description1']
Rate1 = float(input_data['Rate1'])      
VATAmount1 = float(input_data['VATAmount1'])

# First Part Payment

Description2 = input_data['Description2']
Rate2 = float(input_data['Rate2'])      
VATAmount2 = float(input_data['VATAmount2'])

# New Part Payment

now = datetime.now()
desctoday = now.strftime("%d/%m/%Y")
Description3 = """- Part payment of £{} recieved {}
Invoice No: {}""".format(input_data['Payment'], desctoday, input_data['InvoiceNo'])
TotalRate = float(input_data['Payment'])      
RatePrep = TotalRate/1.2
Rate3 = -abs(RatePrep)
VATAmount3 = -abs(TotalRate - RatePrep)

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
        "Number": 1,
        "VATExempt": false,
        "VATLevel": 20.0000,
        "TaxCode": "",
        "Rate":0,
        "VATAmount": 0
    }, {
        "NominalCode": 4906,
        "Description": "",
        "ProductCode": "ANNU0002",
        "Quantity": 1,
        "HomeCurrencyRate": 10.0000,
        "HomeCurrencyVATAmount": 20.0000,
        "Number": 2,
        "VATExempt": false,
        "VATLevel": 20.0000,
        "TaxCode": "",
        "Rate": 0,
        "VATAmount": 0
    }, {
        "NominalCode": 4906,
        "Description": "",
        "ProductCode": "ANNU0002",
        "Quantity": 1,
        "HomeCurrencyRate": 10.0000,
        "HomeCurrencyVATAmount": 20.0000,
        "Number": 0,
        "VATExempt": false,
        "VATLevel": 20.0000,
        "TaxCode": "",
        "Rate": 0,
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
x['LineItems'][2]['Rate'] = Rate3
x['LineItems'][2]['Description'] = Description3
x['LineItems'][2]['VATAmount'] = VATAmount3

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
