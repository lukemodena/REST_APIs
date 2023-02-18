import json
from datetime import date, datetime

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
today = now.strftime("%Y-%m-%d %H:%M:%S +00:00")

my_data = '''
{
    "ActualJournalsAmount":0,
    "ActualPurchasesAmount":0,
    "ActualSalesAmount":"",
    "CustomerCode":"COMPANY_CODE",
    "CustomerName":"COMPANY_NAME",
    "Description":"",
    "StartDate":"",
    "EndDate":"",
    "AssociatedQuotesCount":0,
    "ExcludeVAT":0,
    "Name":"",
    "Note":"",
    "Number":"",
    "Reference":"",
    "Status":1,
    "StatusName":"Active",
    "TargetPurchasesAmount":0,
    "TargetSalesAmount":0,
    "ActualPurchasesVATAmount":0,
    "ActualSalesVATAmount": 0
}
'''
x = json.loads(my_data)
x['StartDate'] = today
x['Name'] = input_data['company']

y = json.dumps(x, indent=4)
my_headers = {
    'Accept' : 'application/json',
    'Content-Type' : 'application/json',
    'Authorization' : input_data['token'],
    'Connection': 'keep-alive',
    'Origin' : 'chrome-extension: //rest-console-id',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22'
}

response = requests.post('https://api.kashflow.com/v2/projects', headers=my_headers, data = y)

output = response.json()
