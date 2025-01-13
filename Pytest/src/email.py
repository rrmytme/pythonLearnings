import sib_api_v3_sdk
from decouple import config
from src.models import Person
from sib_api_v3_sdk.rest import ApiException


configuration = sib_api_v3_sdk.Configuration()
configuration.api_key["api-key"] = config("API_KEY")

# Initialize the SendinBlue API instance
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration)
)

def send_email(person: Person):
    
    subject = "Email from Pytest"
    sender = {"name": "Ridwanray", "email": "hi@ridwanray.com"}
    html_content = f"""Hello {person.name},<br/>
                    Your job title is {person.title}.<br/>
                    Your phone number is {person.phone}"""
    to = [{"email": person.email}]

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to, html_content=html_content, sender=sender, subject=subject
    )
    try:
        # Send the email
        response = api_instance.send_transac_email(send_smtp_email)
        print(f"Email sent to : {person.email}")
    except ApiException as err:
        print(f"Exception when sedinging email: {err}")