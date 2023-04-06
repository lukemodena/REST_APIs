### YOU NEED TO CREATE THE 'Client_Secret.json' AND 'token.pickle' FILES BEFOREHAND ###

from rest_framework.parsers import JSONParser
import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from rest_framework import generics
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated

from django.conf import settings

class eversignAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):

        try: 

            File_Name = self.request.query_params.get('fileName')

            ### CREDENTIALS - Google Drive Integration ###

            CLIENT_SECRET_FILE = settings.CLIENT_SECRET_FILE


            SCOPES = (
                'https://www.googleapis.com/auth/drive.file',
                'https://www.googleapis.com/auth/drive',
                'https://www.googleapis.com/auth/documents',
            )

            cred = None

            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    cred = pickle.load(token)

            if not cred or not cred.valid:
                if cred and cred.expired and cred.refresh_token:
                    cred.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                    cred = flow.run_local_server()

                with open('token.pickle', 'wb') as token:
                    pickle.dump(cred, token)


            DRIVE = build('drive', 'v3', credentials=cred, cache_discovery=False)

            ### Get File ID - From Google Drive ###

            searchQuery = "name='{}'"
            query = searchQuery.format(File_Name)

            page_token = None
            while True:

                response = DRIVE.files().list(q=query,
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)',
                                            pageToken=page_token).execute()

                for file_name in response.get('files', []):
                    # Process change
                    TemplateID=file_name.get('id')
                page_token = response.get('nextPageToken', None)
                if page_token is None:
                    break

            ### Create PDF - From mail merged document on Google Drive, storing locally ###

            File_Location = 'media/Mail_Merge_Documents/{}.pdf'
            
            byteData = DRIVE.files().export_media(
                fileId=TemplateID,
                mimeType='application/pdf'
            ).execute()

            with open(File_Location.format(File_Name), 'wb') as f:
                f.write(byteData)
                f.close()
                
            response = "File successfully saved as PDF"
            
            payload = {
                "response": response,
                "file": File_Location.format(File_Name),
                "data": None
            }

            return JsonResponse(payload,safe=False)

        
        except Exception as e:
        
            response = "Failed to save PDF"

            exc = '{}'.format(e)

            payload = {
                    "response": response,
                    "data": exc
                }

            return JsonResponse(payload,safe=False)
