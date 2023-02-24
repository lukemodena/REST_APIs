# How to run ChatGPT API requests using Django Framework
# Set up Django App as would any other

from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http.response import JsonResponse
from django.conf import settings

import openai

from django.core.files.storage import default_storage

openai.api_key = settings.OPENAI_API_KEY

# Create your views here.
class PhotoAPI(generics.ListAPIView):

    def post(self, request):
        file=request.FILES['myFile']
        file_name=default_storage.save('photos/'+file.name,file)
        file_response="{} saved successfully".format(file_name)

        response = openai.Image.create_variation(
            image=open(f'media/{file_name}', "rb"),
            n=1,
            size="1024x1024"
        )

        image_url = response['data'][0]['url']

        payload = {
            "file_response":file_response,
            "image_url":image_url
        }

        return JsonResponse(payload, safe=False)
