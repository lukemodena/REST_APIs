from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http.response import JsonResponse
from django.conf import settings

import openai

from django.core.files.storage import default_storage

openai.api_key = settings.OPENAI_API_KEY

# Create your views here.

class PromptAPI(generics.ListAPIView):

    def get(self, request):
        prompt=self.request.query_params.get('prompt')
        
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )

        image_url = response['data'][0]['url']

        payload = {
            "image_url":image_url
        }

        return JsonResponse(payload, safe=False)
