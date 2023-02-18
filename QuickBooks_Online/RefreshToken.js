// Create Refresh Token

var authcode = new Buffer(process.env.CLIENT_ID + ":" + process.env.CLIENT_SECRET).toString('base64');

const options = {
  url: `https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer`,
  method: 'POST',
  headers: {
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/json',
    'authorization': "Basic " + authcode
  },
  params: {
    
  },
  body: {
    'grant_type':'refresh_token',
    'refresh_token':bundle.authData.refresh_token
  }
};

return z.request(options)
  .then((response) => {
    response.throwForStatus();
    const results = response.json;

    return results;
  });
