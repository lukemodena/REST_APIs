// Update Estimate with additional line item (Part-Payment)

try {
    // Ensure to get the estimate line items (as a string) before and parse them as a JSON object
  
    const rows = JSON.parse(JSON.parse(`${bundle.inputData.Lines}`).replace(/\\"/g, '"'));
    
    // Create object line item (part payment)
    const newLine = {
        "LineNum": bundle.inputData.LineNumber,
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
    };
    
    // Combine the original line items with the the new Part-Payment line item
    const lines = rows.concat(newLine);

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
        "Line": lines,
        "TxnTaxDetail": {
            "TaxLine": [
            {
                "TaxLineDetail": {
                "TaxRateRef": {
                    "value": "7"
                }
                }
            }
            ]
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

        return results;
    });  
} catch(err) {
    const rows = JSON.parse(`${bundle.inputData.Lines}`);

    const newLine = {
        "LineNum": bundle.inputData.LineNumber,
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
    };
    
    const lines = rows.concat(newLine);

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
        "Line": lines,
        "TxnTaxDetail": {
            "TaxLine": [
            {
                "TaxLineDetail": {
                "TaxRateRef": {
                    "value": "7"
                }
                }
            }
            ]
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

        return results;
    });  

}
