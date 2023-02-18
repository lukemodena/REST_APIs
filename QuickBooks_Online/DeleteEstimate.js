const options = {
  url: `https://quickbooks.api.intuit.com/v3/company/${process.env.COMPANY_ID}/estimate?operation=delete&minorversion=65`,
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
  "Id": `${bundle.inputData.ID}`
  }
}

return z.request(options)
  .then((response) => {
    response.throwForStatus();
    const results = response.json;

    return results;
  });
