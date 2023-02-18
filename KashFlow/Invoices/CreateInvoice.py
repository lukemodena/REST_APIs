import json
from datetime import date, datetime, timedelta

#### FOR PART-PAYMENT ####

# 7 days and unpaid
# Part Payment
# Payment line item not filled 

TotalRate = float(input_data['Payment'])      
Rate1 = TotalRate/1.2
VATAmount1 = TotalRate - Rate1
Tot = float(input_data['Total'])
DescTotal = "£{:,.2f}".format(Tot)
Description1 = """PART PAYMENT:
Part payment of £{} recieved
Associate Fee for R&D Tax relief claim
- Rate {}%
- {}: Fee {}""".format(input_data['Payment'], input_data['COP'], input_data['Reference'], DescTotal)

# Invoice Number

InvoiceNo = int(input_data['InvoiceNo']) + 1

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
today = now.strftime("%Y-%m-%d %H:%M:%S +00:00")
dueprep = now + timedelta(days=7)
due = dueprep.strftime("%Y-%m-%d %H:%M:%S +00:00")
    
my_data = '''
{
    "Address": {
        "CountryCode": "GB",
        "Line1": "Send Barns Stables, Woodhill",
        "Line2": "Send, Woking",
        "Line3": "Surrey",
        "Line4": null,
        "PostCode": "GU23 7JR"
    },
    "AutomaticCreditControlEnabled": true,
    "Currency": {
        "Code": "GBP",
        "ExchangeRate": 1.0000,
        "Name": "British Pounds",
        "Symbol": "£",
        "DisplaySymbolOnRight": false
    },
    "CustomerCode": "RANDD01",
    "CustomerDiscount": 0,
    "CustomerName": COMPANY_NAME,
    "CustomerReference": null,
    "DeliveryAddress": null,
    "DueDate": "",
    "EmailCount": 0,
    "ExchangeRate": 1.0000,
    "GrossAmount": 120.0000,
    "InvoiceInECMemberState": false,
    "InvoiceOutsideECMemberState": true,
    "IssuedDate": "",
    "LineItems": [{
        "ApplyTax1": false,
        "ApplyTax2": false,
        "ApplyTax3": false,
        "ApplyTax4": false,
        "ApplyTax5": false,
        "NominalCode": 4906,
        "Description": "",
        "Number": 0,
        "ProductCode": "ANNU0002",
        "Quantity": 1.0000,
        "Rate": 0.0000,
        "Tax1Amount": 0.0000,
        "Tax2Amount": 0.0000,
        "Tax3Amount": 0.0000,
        "Tax4Amount": 0.0000,
        "Tax5Amount": 0.0000,
        "VATAmount": 20.0000,
        "VATExempt": 0,
        "VATLevel": 20.0000,
        "ProjectNumber": 0
    }],
    "LastPaymentDate": "",
    "NetAmount": 100.0000,
    "Number": 2,
    "OverdueDays": 0,
    "PaidDate": null,
    "Status": "Unpaid",
    "SuppressNumber": 0,
    "TotalPaidAmount": 0,
    "UpdateCustomerAddress": false,
    "UpdateCustomerDeliveryAddress": false,
    "UseCustomDeliveryAddress": false,
    "VATAmount": 20.000,
    "VATNumber": "",
    "PayOnlinePaymentProcessor": 0
}
'''
x = json.loads(my_data)
x['LastPaymentDate'] = today
x['IssuedDate'] = today
x['Number'] = InvoiceNo
x['DueDate'] = due
x['CustomerReference'] = input_data['Reference']
x['ProjectNumber'] = int(input_data['projectno'])
x['TotalPaidAmount'] = Rate1
x['LineItems'][0]['Rate'] = Rate1
x['LineItems'][0]['Description'] = Description1
x['LineItems'][0]['VATAmount'] = VATAmount1




y = json.dumps(x, indent=4)
my_headers = {
    'Accept' : 'application/json',
    'Content-Type' : 'application/json',
    'Authorization' : input_data['token'],
    'Connection': 'keep-alive',
    'Origin' : 'chrome-extension: //rest-console-id',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22'
}

response = requests.post('https://api.kashflow.com/v2/invoices', headers=my_headers, data = y)

output = response.json()
