import json

my_headers = {
    'Accept' : 'application/json',
    'Content-Type' : 'application/json',
    'Authorization' : input_data['token'],
    'Connection': 'keep-alive',
    'Origin' : 'chrome-extension: //rest-console-id',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22'
}
response = requests.get(f'https://api.kashflow.com/v2/quotes/{input_data['QuoteID']}', headers=my_headers)

### 2nd PP
try:
    x = response.json()["LineItems"][3]["Description"]
    SndPartpaymentExists = True
    
    ### 3rd PP
    try:
        y = response.json()["LineItems"][4]["Description"]
        TrdPartpaymentExists = True
        
        ### 4th PP
        try:
            z = response.json()["LineItems"][5]["Description"]
            FrthPartpaymentExists = True
            
            ### 5th PP
            try:
                q = response.json()["LineItems"][6]["Description"]
                FfthPartpaymentExists = True
                output = [{"2nd Part-payment Exists": SndPartpaymentExists, "3rd Part-payment Exists": TrdPartpaymentExists, "4th Part-payment Exists": FrthPartpaymentExists, "5th Part-payment Exists": FfthPartpaymentExists, "DescriptionPP2": response.json()["LineItems"][3]["Description"], "RatePP2": response.json()["LineItems"][3]["Rate"], "VATAmountPP2": response.json()["LineItems"][3]["VATAmount"], "NumberPP2": response.json()["LineItems"][3]["Number"], "DescriptionPP3": response.json()["LineItems"][4]["Description"], "RatePP3": response.json()["LineItems"][4]["Rate"], "VATAmountPP3": response.json()["LineItems"][4]["VATAmount"], "NumberPP3": response.json()["LineItems"][4]["Number"], "DescriptionPP4": response.json()["LineItems"][5]["Description"], "RatePP4": response.json()["LineItems"][5]["Rate"], "VATAmountPP4": response.json()["LineItems"][5]["VATAmount"], "NumberPP4": response.json()["LineItems"][5]["Number"], "DescriptionPP5": response.json()["LineItems"][6]["Description"], "RatePP5": response.json()["LineItems"][6]["Rate"], "VATAmountPP5": response.json()["LineItems"][6]["VATAmount"], "NumberPP5": response.json()["LineItems"][6]["Number"]}]
                return output
            
            ### 5th PP Doesn't Exist
            except:
                output = [{"2nd Part-payment Exists": SndPartpaymentExists, "3rd Part-payment Exists": TrdPartpaymentExists, "4th Part-payment Exists": FrthPartpaymentExists, "5th Part-payment Exists": False, "DescriptionPP2": response.json()["LineItems"][3]["Description"], "RatePP2": response.json()["LineItems"][3]["Rate"], "VATAmountPP2": response.json()["LineItems"][3]["VATAmount"], "NumberPP2": response.json()["LineItems"][3]["Number"], "DescriptionPP3": response.json()["LineItems"][4]["Description"], "RatePP3": response.json()["LineItems"][4]["Rate"], "VATAmountPP3": response.json()["LineItems"][4]["VATAmount"], "NumberPP3": response.json()["LineItems"][4]["Number"], "DescriptionPP4": response.json()["LineItems"][5]["Description"], "RatePP4": response.json()["LineItems"][5]["Rate"], "VATAmountPP4": response.json()["LineItems"][5]["VATAmount"], "NumberPP4": response.json()["LineItems"][5]["Number"]}]
                return output
        
        ### 4th PP Doesn't Exist
        except:
            output = [{"2nd Part-payment Exists": SndPartpaymentExists, "3rd Part-payment Exists": TrdPartpaymentExists, "4th Part-payment Exists": False, "5th Part-payment Exists": False, "DescriptionPP2": response.json()["LineItems"][3]["Description"], "RatePP2": response.json()["LineItems"][3]["Rate"], "VATAmountPP2": response.json()["LineItems"][3]["VATAmount"], "NumberPP2": response.json()["LineItems"][3]["Number"], "DescriptionPP3": response.json()["LineItems"][4]["Description"], "RatePP3": response.json()["LineItems"][4]["Rate"], "VATAmountPP3": response.json()["LineItems"][4]["VATAmount"], "NumberPP3": response.json()["LineItems"][4]["Number"]}]
            return output
        
    ### 3rd PP Doesn't Exist
    except:
        output = [{"2nd Part-payment Exists": SndPartpaymentExists, "3rd Part-payment Exists": False, "4th Part-payment Exists": False, "5th Part-payment Exists": False, "DescriptionPP2": response.json()["LineItems"][3]["Description"], "RatePP2": response.json()["LineItems"][3]["Rate"], "VATAmountPP2": response.json()["LineItems"][3]["VATAmount"], "NumberPP2": response.json()["LineItems"][3]["Number"]}]
        return output
    
### 2nd PP Doesn't Exist
except:
    output = [{"2nd Part-payment Exists": False, "3rd Part-payment Exists": False, "4th Part-payment Exists": False, "5th Part-payment Exists": False}]
    return output
