const url = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${process.env.CLIENT_ID}&redirect_uri=${encodeURIComponent(bundle.inputData.redirect_uri)}&response_type=code&scope=https://www.googleapis.com/auth/drive&access_type=offline&prompt=consent`;

return url;
