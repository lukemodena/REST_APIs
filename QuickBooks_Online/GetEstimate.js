// GET request for Estimate on QuickBooks Online

const options = {
  url: `https://quickbooks.api.intuit.com/v3/company/${process.env.COMPANY_ID}/estimate/${bundle.inputData.ID}?minorversion=65`,
  method: 'GET',
  headers: {
'Authorization': `Bearer ${bundle.authData.access_token}`,
 'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/json'
  },
  params: {

  },
  body: {

  }
};

return z.request(options)
  .then((response) => {
    response.throwForStatus();
    const results = z.JSON.parse(response.content);
  
    // Prepare results data
    
    const length = results["Estimate"]["Line"].length
    
    const linesLength = length - 1
    
    const rows = [];
    for (let i = 0; i < linesLength; i++) {
        rows.push(results["Estimate"]["Line"][i]);
    }
    const line1 = results["Estimate"]["Line"][0];
    const line2 = results["Estimate"]["Line"][1];
    const strline1 = JSON.stringify(results["Estimate"]["Line"][0]);
    const strline2 = JSON.stringify(results["Estimate"]["Line"][1]);
    const lines =  JSON.stringify(rows);
    const ref = results["Estimate"]["CustomField"][1];
    const tax = results["Estimate"]["TxnTaxDetail"]["TaxLine"][0];
    
    const finalRes = {"results": results, "length": length, "lines": lines, "line1": line1, "str1": strline1, "str2": strline2, "line2": line2, "Reference": ref, "newTax": tax};

 

    return finalRes;
  });
