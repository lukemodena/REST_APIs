### FIRST APP + API INTEGRATION BUILT IN 2021 ###

from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests

import sys
sys.path.append("..")
import eversign

from apiclient.http import MediaFileUpload
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

from flask import Flask, request, Response
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class ClientModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    address_1 = db.Column(db.String(100), nullable=False)
    address_2 = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(100), nullable=False)
    end_date = db.Column(db.String(100), nullable=False)
    cfr = db.Column(db.String(100), nullable=False)
    mf = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    terms_name = db.Column(db.String(100), nullable=False)
    consultant_name = db.Column(db.String(100), nullable=False)
    consultant_email = db.Column(db.String(100), nullable=False)
    money_launder = db.Column(db.String(100), nullable=False)

    def  __repr__(self):
        return f"Client(first_name={first_name}, last_name={last_name}, address_1={address_1}, address_2={address_2}, city={city}, postal_code={postal_code}, date={date}, start_date={start_date}, end_date={end_date}, cfr={cfr}, last_name={last_name}, mf={mf}, company_name={company_name}, email={email}, terms_name={terms_name}, consultant_name={consultant_name}, consultant_email={consultant_email}, money_launder={money_launder})"

db.create_all()

client_put_args = reqparse.RequestParser()
client_put_args.add_argument("first_name", type=str, help="First name is required", required=True)
client_put_args.add_argument("last_name", type=str, help="Last name is required", required=True)
client_put_args.add_argument("address_1", type=str, help="Address 1 is required", required=True)
client_put_args.add_argument("address_2", type=str, help="Address 2 is required", required=True)
client_put_args.add_argument("city", type=str, help="City is required", required=True)
client_put_args.add_argument("postal_code", type=str, help="Postcode is required", required=True)
client_put_args.add_argument("date", type=str, help="Date is required", required=True)
client_put_args.add_argument("start_date", type=str, help="Start date is required", required=True)
client_put_args.add_argument("end_date", type=str, help="End date is required", required=True)
client_put_args.add_argument("cfr", type=str, help="CFR is required", required=True)
client_put_args.add_argument("mf", type=str, help="MF is required", required=True)
client_put_args.add_argument("company_name", type=str, help="Company name is required", required=True)
client_put_args.add_argument("email", type=str, help="Email is required", required=True)
client_put_args.add_argument("terms_name", type=str, help="Terms name is required", required=True)
client_put_args.add_argument("consultant_name", type=str, help="Consultant name is required", required=True)
client_put_args.add_argument("consultant_email", type=str, help="Consultant email is required", required=True)
client_put_args.add_argument("money_launder", type=str, help="Money laundering option is required", required=True)

client_update_args = reqparse.RequestParser()
client_update_args.add_argument("first_name", type=str, help="First name is required")
client_update_args.add_argument("last_name", type=str, help="Last name is required")
client_update_args.add_argument("address_1", type=str, help="Address 1 is required")
client_update_args.add_argument("address_2", type=str, help="Address 2 is required")
client_update_args.add_argument("city", type=str, help="City is required")
client_update_args.add_argument("postal_code", type=str, help="Postcode is required")
client_update_args.add_argument("date", type=str, help="Date is required")
client_update_args.add_argument("start_date", type=str, help="Start date is required")
client_update_args.add_argument("end_date", type=str, help="End date is required")
client_update_args.add_argument("cfr", type=str, help="CFR is required")
client_update_args.add_argument("mf", type=str, help="MF is required")
client_update_args.add_argument("company_name", type=str, help="Company name is required")
client_update_args.add_argument("email", type=str, help="Email is required")
client_update_args.add_argument("terms_name", type=str, help="Terms name is required")
client_update_args.add_argument("consultant_name", type=str, help="Consultant name is required")
client_update_args.add_argument("consultant_email", type=str, help="Consultant email is required")
client_update_args.add_argument("money_launder", type=str, help="Money laundering option is required")

resource_fields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'address_1': fields.String,
    'address_2': fields.String,
    'city': fields.String,
    'postal_code': fields.String,
    'date': fields.String,
    'start_date': fields.String,
    'end_date': fields.String,
    'cfr': fields.String,
    'mf': fields.String,
    'company_name': fields.String,
    'email': fields.String,
    'terms_name': fields.String,
    'consultant_name': fields.String,
    'consultant_email': fields.String,
    'money_launder': fields.String
}

class Client(Resource):
    @marshal_with(resource_fields)
    def get(self, client_id):
        result = ClientModel.query.filter_by(id=client_id).first()
        if not result:
            abort(404, message="Could not find client with that ID...")
        return result

    @marshal_with(resource_fields)
    def put(self, client_id):
        args = client_put_args.parse_args()
        result = ClientModel.query.filter_by(id=client_id).first()
        if result:
            abort(409, message="Client ID taken...")

        client = ClientModel(id=client_id, first_name=args['first_name'], last_name=args['last_name'], address_1=args['address_1'], address_2=args['address_2'], city=args['city'], postal_code=args['postal_code'], date=args['date'], start_date=args['start_date'], end_date=args['end_date'], cfr=args['cfr'], mf=args['mf'], company_name=args['company_name'], email=args['email'], terms_name=args['terms_name'], consultant_name=args['consultant_name'], consultant_email=args['consultant_email'], money_launder=args['money_launder'])
        db.session.add(client)
        db.session.commit()
        return client, 201

    @marshal_with(resource_fields)
    def patch(self, client_id):
        args = client_update_args.parse_args()
        result = ClientModel.query.filter_by(id=client_id).first()
        if not result:
            abort(404, message="Could not find client with that ID, cannot update...")

        if args["first_name"]:
            result.first_name = args['first_name']
        if args["last_name"]:
            result.last_name = args['last_name']
        if args["address_1"]:
            result.address_1 = args['address_1']
        if args["address_2"]:
            result.address_2 = args['address_2']
        if args["city"]:
            result.city = args['city']
        if args["postal_code"]:
            result.postal_code = args['postal_code']
        if args["date"]:
            result.date = args['date']
        if args["start_date"]:
            result.start_date = args['start_date']
        if args["end_date"]:
            result.end_date = args['end_date']
        if args["cfr"]:
            result.cfr = args['cfr']
        if args["mf"]:
            result.mf = args['mf']
        if args["company_name"]:
            result.company_name = args['company_name']
        if args["email"]:
            result.email = args['email']
        if args["terms_name"]:
            result.terms_name = args['terms_name']
        if args["consultant_name"]:
            result.consultant_name = args['consultant_name']
        if args["consultant_email"]:
            result.consultant_email = args['consultant_email']
        if args["money_launder"]:
            result.money_launder = args['money_launder']

        db.session.commit()

        return result

api.add_resource(Client, "/client/<int:client_id>")

@app.route('/webhooks', methods=['PATCH'])
def respond():
    print(request.json);
    return Response(status=200)

@app.route('/client/0/json-example', methods=['PATCH'])
def json_example():
    request_data = request.json

    date_today = date.today().strftime("%d/%m/%Y")

    firstname = request_data['first_name']
    lastname = request_data['last_name']
    address1 = request_data['address_1']
    address2 = request_data['address_2']
    cit = request_data['city']
    postalcode = request_data['postal_code']
    tdate = date_today
    startdate = request_data['start_date']
    enddate = request_data['end_date']
    cfeer = request_data['cfr']
    mfee = request_data['mf']
    companyname = request_data['company_name']
    e_mail = request_data['email']
    termsname = request_data['terms_name']
    consultantname = request_data['consultant_name']
    consultantemail = request_data['consultant_email']
    moneylaunder = request_data['money_launder']

    BASE = "https://WEBHOST.BASE.com/"

    response = requests.patch(BASE + "client/0", {"first_name": firstname, "last_name": lastname, "address_1": address1, "address_2": address2, "city": cit, "postal_code": postalcode, "date": tdate, "start_date": startdate, "end_date": enddate, "cfr": cfeer, "mf": mfee, "company_name": companyname, "email": e_mail, "terms_name": termsname, "consultant_name": consultantname, "consultant_email": consultantemail, "money_launder": moneylaunder})

    return '''
           The first name value is: {}
           The last name value is: {}
           The dataset is: {}'''.format(firstname, lastname, response.json())

@app.route('/client/0/eversign', methods=['GET'])
def eversignwebhook():

    ### CREDENTIALS ###

    CLIENT_SECRET_FILE = 'Client_Secret.json'

    SCOPES = (
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/documents',
        'https://www.googleapis.com/auth/spreadsheets.readonly'
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

    ### Get Client ###

    BASE = "https://WEBHOST.BASE.com/"

    response = requests.get(BASE + "client/0")

    ### Input Data ###

    Fname = response.json()['first_name']

    Lname = response.json()['last_name']

    Company = response.json()['company_name']

    Main_contact_email = response.json()['email']

    Terms_name = response.json()['terms_name']

    Consultant = response.json()['consultant_name']

    Consultant_email = response.json()['consultant_email']

    Money_laundering = response.json()['money_launder']


    Main_contact = Fname + " " + Lname

    Subject = "R&D Tax Relief Terms Between {} and *COMPANY NAME*"

    if Money_laundering == "Yes":
        email_cont = "Please review and sign your contract with *COMPANY NAME* and complete the Anti Money Laundering ID form also included, by selecting the \"Review & Sign\" link above in this email"
    elif Money_laundering =="No":
        email_cont = "Please review and sign your contract with *COMPANY NAME* by selecting the \"Review & Sign\" link above in this email"

    ### Get File ID ###

    searchQuery = "name='{}'"
    query = searchQuery.format(Terms_name)

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

    ### Create PDF ###

    File_Location = 'Mail_Merge_Documents/{}.pdf'

    New_File_ID = TemplateID

    byteData = DRIVE.files().export_media(
        fileId=New_File_ID,
        mimeType='application/pdf'
    ).execute()

    with open(File_Location.format(Terms_name), 'wb') as f:
        f.write(byteData)
        f.close()

    ### EVERSIGN ###

    eversign_client = eversign.Client(process.env.EVERSIGN_CLIENT)

    eversign_client.set_selected_business_by_id(process.env.BUSINESS_ID)

    document = eversign.Document()
    document.title = Subject.format(Company)
    document.message = email_cont
    document.sandbox = False
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

        finished_document = eversign_client.create_document(document)

    except Exception:
        pass

    return '''{}'''.format(TemplateID)

if __name__ == '__main__':
    app.run()
