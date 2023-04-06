import eversign

from rest_framework import generics
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated

from documentApp.models import EversignForm
from documentApp.serializers import EversignFormSerializer

from django.conf import settings

class eversignAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):

        try: 

            customer_form_id = int(self.request.query_params.get('id'))

            ### Get Client - Stored on Local database ###
            
            form_info = EversignForm.objects.get(id=customer_form_id)
            form_serializer = EversignFormSerializer(form_info)

            serialized_form_info = form_serializer.data


            ### Prepare Input Data - for eversign documentation ###

            Fname = serialized_form_info['first_name']

            Lname = serialized_form_info['last_name']

            Company = serialized_form_info['company_name']

            Main_contact_email = serialized_form_info['email']

            Terms_name = serialized_form_info['terms_name']

            Consultant = serialized_form_info['consultant_name']

            Consultant_email = serialized_form_info['consultant_email']

            Money_laundering = serialized_form_info['money_launder']


            Main_contact = Fname + " " + Lname

            Subject = "R&D Tax Relief Terms Between {} and {}"

            if Money_laundering == "Yes":
                email_cont = f"Please review and sign your contract with {settings.COMPANY_NAME} and complete the Anti Money Laundering ID form also included, by selecting the \"Review & Sign\" link above in this email"
            elif Money_laundering =="No":
                email_cont = f"Please review and sign your contract with {settings.COMPANY_NAME} by selecting the \"Review & Sign\" link above in this email"

            ### Get PDF - Insert your PDF GET method here ###

            File_Location = 'media/Mail_Merge_Documents/{}.pdf'
            Terms_Name = settings.TERMS_NAME
            
            ### EVERSIGN ###

            eversign_client = eversign.Client(settings.EVERSIGN_CLIENT_ID)

            eversign_client.set_selected_business_by_id(settings.EVERSIGN_BUSINESS_ID)

            document = eversign.Document()
            document.title = Subject.format(Company, settings.COMPANY_NAME)
            document.message = email_cont
            document.sandbox = True
            document.use_hidden_tags = True
            document.use_signer_order = True
            document.require_all_signers = True

            eversign_file = eversign.File(name=Terms_name)
            eversign_file.file_url = File_Location.format(Terms_name)

            try:

                signer = eversign.Signer()
                signer.id = "1"
                signer.name = Main_contact
                signer.email = Main_contact_email
                signer.order = 1

                signer2 = eversign.Signer()
                signer2.id = "2"
                signer2.name = Consultant
                signer2.email = Consultant_email
                signer2.order = 2

                # To get embedded_claim_url in response, document has to be created as a draft
                # document.is_draft = True

                document.add_file(eversign_file)
                document.add_signer(signer)
                document.add_signer(signer2)

                eversign_client.create_document(document)

                response = "Successfully created eversign document"

                payload = {
                    "response": response,
                    "file": File_Location.format(Terms_name),
                    "data": None
                }

                return JsonResponse(payload,safe=False)

            except Exception:
                pass

            response = "Failed to create eversign document"

            payload = {
                "response": response,
                "data": None
            }

            return JsonResponse(payload,safe=False)
        
        except Exception as e:
            response = "Failed to create eversign document"

            exc = '{}'.format(e)

            payload = {
                    "response": response,
                    "data": exc
                }

            return JsonResponse(payload,safe=False)
        
