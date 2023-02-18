const options = {
  url: `https://www.googleapis.com/drive/v3/files/${bundle.inputData.id}`,
  method: 'DELETE',
  headers: {
    'Authorization': `Bearer ${bundle.inputData.token}`
  },
  params: {

  },
  body: {

  }
}

return z.request(options)
  .then((response) => {
    response.throwForStatus();
    const results = response.json;

    return {"Results": results, "Document": "Deleted Successfully"};
  });
