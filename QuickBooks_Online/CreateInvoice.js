// Create (POST) Invoice on QuickBooks Online

const options = {
  url: `https://quickbooks.api.intuit.com/v3/company/${process.env.COMPANY_ID}/invoice?minorversion=65`,
  method: 'POST',
  headers: {
'Authorization': `Bearer ${bundle.authData.access_token}`,
 'content-type': 'application/json',
    'accept': 'application/json'
  },
  params: {

  },
  body: {
    "CustomerMemo": {
      "value": `${bundle.inputData.Reference}`
    },
    "PrivateNote": `${bundle.inputData.Reference}`,
    "CustomField": [
     {
      "DefinitionId": "2",
      "Name": "Quote Stage",
      "Type": "StringType",
      "StringValue": "5 Invoiced"
     },
     {
       "DefinitionId": "3",
       "Name": "Estimate Ref",
       "Type": "StringType",
       "StringValue": `Part Payment - ${bundle.inputData.ShortReference}`,
     }
    ],
    "PrintStatus": "NeedToPrint", 
    "EmailStatus": "NotSet", 
     "Line": [
     {
      "Id": "1",
      "LineNum": 1,
      "Description": `${bundle.inputData.Description}`,
      "Amount": bundle.inputData.Amount,
      "DetailType": "SalesItemLineDetail",
      "SalesItemLineDetail": {
       "ItemRef": {
        "value": "5",
        "name": "Annual Claim Fee (Part Payment)"
       },
       "UnitPrice": bundle.inputData.Amount,
       "Qty": 1,
       "ItemAccountRef": {
        "value": "4",
        "name": "Sales"
       },
       "TaxCodeRef": {
        "value": "6"
       }
      }
     },
     {
      "DetailType": "SubTotalLineDetail",
      "SubTotalLineDetail": {}
     }
    ],
    "CustomerRef": {
      "name": `${bundle.inputData.Name}`, 
      "value": `${bundle.inputData.ID}`
    }, 
    "TxnTaxDetail": {
      "TotalTax": 0
    }, 
    "ApplyTaxAfterDiscount": false
  }
}

return z.request(options)
  .then((response) => {
    response.throwForStatus();
    const results = z.JSON.parse(response.content);

    return results;
  });
