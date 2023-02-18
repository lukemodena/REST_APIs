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

// Work out whether a first or second Estimate line item

if (bundle.inputData.LineNumber === "1"){
    try {
        const lines = JSON.parse(JSON.parse(`${bundle.inputData.Lines}`).replace(/\\"/g, '"'));
        
        lines[0]["Description"] = `${bundle.inputData.Description}`;
        lines[0]["Amount"] = parseFloat(bundle.inputData.Amount);
        lines[0]["SalesItemLineDetail"]["UnitPrice"] = parseFloat(bundle.inputData.Amount);

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
              "SyncToken": `${bundle.inputData.SyncToken}`, 
              "domain": "QBO", 
              "sparse": true, 
              "Id": `${bundle.inputData.ID}`, 
              "BillEmail": {
                "Address": getEmail(bundle.inputData.CustomerRefName)
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
              "Line": lines,
              "TxnTaxDetail": {
                "TotalTax": parseFloat(bundle.inputData.TaxAmount),
              },
              "CustomerRef": {
                "name": `${bundle.inputData.CustomerRefName}`, 
                "value": `${bundle.inputData.CustomerRef}`
              }, 
            }
          };
      
          return z.request(options)
              .then((response) => {
                response.throwForStatus();
                const results = z.JSON.parse(response.content);
      
                // You can do any parsing you need for results here before returning them
      
                return results;
        });
    } catch (err) {
        var lines = JSON.parse(`${bundle.inputData.Lines}`);

        lines[0]["Description"] = `${bundle.inputData.Description}`;
        lines[0]["Amount"] = parseFloat(bundle.inputData.Amount);
        lines[0]["SalesItemLineDetail"]["UnitPrice"] = parseFloat(bundle.inputData.Amount);

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
              "SyncToken": `${bundle.inputData.SyncToken}`, 
              "domain": "QBO", 
              "sparse": true, 
              "Id": `${bundle.inputData.ID}`,
              "BillEmail": {
                "Address": getEmail(bundle.inputData.CustomerRefName) 
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
              "Line": lines,
              "TxnTaxDetail": {
                "TotalTax": parseFloat(bundle.inputData.TaxAmount),
              },
              "CustomerRef": {
                "name": `${bundle.inputData.CustomerRefName}`, 
                "value": `${bundle.inputData.CustomerRef}`
              }, 
            }
          };
      
          return z.request(options)
              .then((response) => {
                response.throwForStatus();
                const results = z.JSON.parse(response.content);
      
                // You can do any parsing you need for results here before returning them
      
                return results;
        });
    }
  } else if (bundle.inputData.LineNumber === "2"){
    try {
        var lines = JSON.parse(JSON.parse(`${bundle.inputData.Lines}`).replace(/\\"/g, '"'));

        lines[1]["Description"] = `${bundle.inputData.Description}`;
        lines[1]["Amount"] = parseFloat(bundle.inputData.Amount);
        lines[1]["SalesItemLineDetail"]["UnitPrice"] = parseFloat(bundle.inputData.Amount);

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
              "SyncToken": `${bundle.inputData.SyncToken}`, 
              "domain": "QBO", 
              "sparse": true, 
              "Id": `${bundle.inputData.ID}`, 
              "BillEmail": {
                "Address": getEmail(bundle.inputData.CustomerRefName)
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
              "Line": lines,
              "TxnTaxDetail": {
                "TotalTax": parseFloat(bundle.inputData.TaxAmount),
              },
              "CustomerRef": {
                "name": `${bundle.inputData.CustomerRefName}`, 
                "value": `${bundle.inputData.CustomerRef}`
              }, 
            }
          };
      
          return z.request(options)
              .then((response) => {
                response.throwForStatus();
                const results = z.JSON.parse(response.content);
      
                // You can do any parsing you need for results here before returning them
      
                return results;
        });
    
    } catch(err) {
        var lines = JSON.parse(`${bundle.inputData.Lines}`);

        lines[1]["Description"] = `${bundle.inputData.Description}`;
        lines[1]["Amount"] = parseFloat(bundle.inputData.Amount);
        lines[1]["SalesItemLineDetail"]["UnitPrice"] = parseFloat(bundle.inputData.Amount);

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
              "SyncToken": `${bundle.inputData.SyncToken}`, 
              "domain": "QBO", 
              "sparse": true, 
              "Id": `${bundle.inputData.ID}`, 
              "BillEmail": {
                "Address": getEmail(bundle.inputData.CustomerRefName)
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
              "Line": lines,
              "TxnTaxDetail": {
                "TotalTax": parseFloat(bundle.inputData.TaxAmount),
              },
              "CustomerRef": {
                "name": `${bundle.inputData.CustomerRefName}`, 
                "value": `${bundle.inputData.CustomerRef}`
              }, 
            }
          };
      
          return z.request(options)
              .then((response) => {
                response.throwForStatus();
                const results = z.JSON.parse(response.content);
      
                // You can do any parsing you need for results here before returning them
      
                return results;
        });

    }
}
