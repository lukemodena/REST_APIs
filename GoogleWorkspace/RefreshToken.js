const options = {
  url: 'https://oauth2.googleapis.com/token',
  method: 'POST',
  headers: {
    'host': 'oauth2.googleapis.com',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/json'
  },
  params: {

  },
  body: {
    'client_id': process.env.CLIENT_ID,
    'client_secret': process.env.CLIENT_SECRET,
    'refresh_token': bundle.authData.refresh_token,
    'grant_type': 'refresh_token'
  }
}

return z.request(options)
  .then((response) => {
    response.throwForStatus();
    const results = response.json;

    // You can do any parsing you need for results here before returning them

    return results;
  });
