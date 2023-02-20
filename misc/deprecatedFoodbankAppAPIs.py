## Original Participant List API used a loop funtion to find donors associated with a participant in list (using foreign key)

## This method could be unpredictable if the search values were irregular, now the foreign key is handled within the serializer.

class OLDParticipantListApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]

    def get(self, request):
        type = self.request.query_params.get('type')
        collId = self.request.query_params.get('collid')
        page = self.request.query_params.get('page')


        if collId is not None:
            if type is not None:
                if type == "1":
                    allParticipants = Participation.objects.filter(CollectionID=collId).order_by('DropOffTime')

                elif type == "2":
                    allParticipants = Participation.objects.filter(CollectionID=collId).order_by('-TotalDonated')

                elif type == "4":
                    allParticipants = Participation.objects.filter(CollectionID=collId).order_by('DropOffTime')

                else:
                    allParticipants = Participation.objects.filter(CollectionID=collId)
            else:
                allParticipants = Participation.objects.filter(CollectionID=collId)
        else:

            if type is not None:
                if type == "1":
                    allParticipants = Participation.objects.all().order_by('DropOffTime')

                elif type == "2":
                    allParticipants = Participation.objects.all().order_by('-TotalDonated')

                elif type == "4":
                    allParticipants = Participation.objects.all().order_by('DropOffTime')

                else:
                    allParticipants = Participation.objects.all()
            else:
                allParticipants = Participation.objects.all()
        participants = allParticipants.values_list('DonorID', flat=True)
        partID = allParticipants.values_list('ParticipationID', flat=True)
        participants = list(participants)
        partID = list(partID)
        
        fullname = self.request.query_params.get('fullname')

        if fullname is not None:
            donorsqueryset = Donor.objects.all().filter(FullName__icontains=fullname)
        else:
            donorsqueryset = Donor.objects.all()

        if type is not None:
            participantsqueryset = Participation.objects.all().filter(DonationType__icontains=type)
        else:
            participantsqueryset = Participation.objects.all() 

        length = len(participants)
        donors = []
        for i in range(length):
            try:
                donor = donorsqueryset.get(DonorID=participants[i])
                participant = participantsqueryset.get(ParticipationID=partID[i])
                serializedDonor = DonorSerializer(donor)
                serializedParticipant = ParticipationSerializer(participant)


                x = {
                        "ParticipationID": "{}".format(serializedParticipant.data['ParticipationID']), 
                        "DonorID": "{}".format(serializedDonor.data['DonorID']), 
                        "WholesaleID": "{}".format(serializedParticipant.data['WholesaleID']),
                        "CollectionID": "{}".format(serializedParticipant.data['CollectionID']),
                        "FullName": "{}".format(serializedDonor.data['FullName']), 
                        "Email": "{}".format(serializedDonor.data['Email']), 
                        "Phone": "{}".format(serializedDonor.data['Phone']), 
                        "Notes": "{}".format(serializedDonor.data['Notes']), 
                        "ParticipationNotes": "{}".format(serializedParticipant.data['Notes']),
                        "Address1": "{}".format(serializedDonor.data['Address1']), 
                        "Address2": "{}".format(serializedDonor.data['Address2']), 
                        "PostCode": "{}".format(serializedDonor.data['PostCode']), 
                        "DonationType": "{}".format(serializedParticipant.data['DonationType']),
                        "TotalDonated": "{}".format(serializedParticipant.data['TotalDonated']),
                        "DropOffTime": "{}".format(serializedParticipant.data['DropOffTime']),
                        "PaymentRecieved": "{}".format(serializedParticipant.data['PaymentRecieved']).lower() 
                    }
                donors.append(x)
            except:
                pass

        return JsonResponse(donors, safe=False)
