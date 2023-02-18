// Get Main Invoicing Customer Email

const getEmail = (inputValue) => {
  if (inputValue === "COMPANY_NAME_1") {
    let email = "email1@emailaddress.com";
    return email;
  } else if (inputValue === "COMPANY_NAME_2") {
    let email = "email2@emailaddress.com"
    return email
  } else if (inputValue === "COMPANY_NAME_3") {
    let email = "email3@emailaddress.com"
    return email
  } else {
    let email = "email3@emailaddress.com"
    return email
  }
};

// Work out whether a single year or two year claim

if (bundle.inputData.Second === true){
  const options = {
  url: `https://quickbooks.api.intuit.com/v3/company/${process.env.COMPANY_ID}/estimate?minorversion=65`,
  method: 'POST',
  headers: {
'Authorization': `Bearer ${bundle.authData.access_token}`,
 'content-type': 'application/json',
    'accept': 'application/json'
  },
  params: {

  },
  body: {
    "BillEmail": {
      "Address": getEmail(bundle.inputData.Name)
    }, 
    "CustomerMemo": {
      "value": `${bundle.inputData.Reference}`
    },
    "PrivateNote": `${bundle.inputData.Reference}`,
    "CustomField": [
     {
      "DefinitionId": "2",
      "Name": "Quote Stage",
      "Type": "StringType",
      "StringValue": `${bundle.inputData.Stage}`
     },
     {
      "DefinitionId": "3",
      "Name": "Estimate Ref",
      "Type": "StringType",
      "StringValue": `${bundle.inputData.ShortReference}`
     }
    ],
    "PrintStatus": "NeedToPrint", 
    "EmailStatus": "NotSet",  
     "Line": [
     {
      "Id": "1",
      "LineNum": 1,
      "Description": `${bundle.inputData.FirstDescription}`,
      "Amount": bundle.inputData.FirstAmount,
      "DetailType": "SalesItemLineDetail",
      "SalesItemLineDetail": {
       "ItemRef": {
        "value": "3",
        "name": "Annual Claim Fee (A)"
       },
       "UnitPrice": bundle.inputData.FirstAmount,
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
      "Id": "3",
      "LineNum": 2,
      "Description": `${bundle.inputData.SecondDescription}`,
      "Amount": bundle.inputData.SecondAmount,
      "DetailType": "SalesItemLineDetail",
      "SalesItemLineDetail": {
       "ItemRef": {
        "value": "4",
        "name": "Annual Claim Fee (B)"
       },
       "UnitPrice": bundle.inputData.SecondAmount,
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
};

return z.request(options)
  .then((response) => {
    response.throwForStatus();
    const results = z.JSON.parse(response.content);

    return results;
  });
} else {
  const options = {
    url: `https://quickbooks.api.intuit.com/v3/company/${process.env.COMPANY_ID}/estimate?minorversion=65`,
    method: 'POST',
    headers: {
  'Authorization': `Bearer ${bundle.authData.access_token}`,
   'content-type': 'application/json',
      'accept': 'application/json'
    },
    params: {
  
    },
    body: {
      "BillEmail": {
        "Address": getEmail(bundle.inputData.Name)
      }, 
      "CustomerMemo": {
        "value": `${bundle.inputData.Reference}`
      },
      "PrivateNote": `${bundle.inputData.Reference}`,
      "CustomField": [
       {
        "DefinitionId": "2",
        "Name": "Quote Stage",
        "Type": "StringType",
        "StringValue": `${bundle.inputData.Stage}`
       },
       {
        "DefinitionId": "3",
        "Name": "Estimate Ref",
        "Type": "StringType",
        "StringValue": `${bundle.inputData.ShortReference}`
       }
      ],
      "PrintStatus": "NeedToPrint", 
      "EmailStatus": "NotSet",  
       "Line": [
       {
        "Id": "1",
        "LineNum": 1,
        "Description": `${bundle.inputData.FirstDescription}`,
        "Amount": bundle.inputData.FirstAmount,
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
         "ItemRef": {
          "value": "3",
          "name": "Annual Claim Fee (A)"
         },
         "UnitPrice": bundle.inputData.FirstAmount,
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
        "Amount": bundle.inputData.FirstAmount,
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
  };
  
  return z.request(options)
    .then((response) => {
      response.throwForStatus();
      const results = z.JSON.parse(response.content);
  
      return results;
    });
};
