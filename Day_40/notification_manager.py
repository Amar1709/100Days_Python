from twilio.rest import Client
from SMTPEmail import smtplib

TWILIO_SID = "TWILIO_SID"   # Your Twilio SID
TWILIO_AUTH_TOKEN = "TWILIO_AUTH_TOKEN" # Your Twilio Auth Token
TWILIO_VIRTUAL_NUMBER = "+1 12345 67890" # Your Twilio Virtual Number
TWILIO_VERIFIED_NUMBER = "+1 12345 67890" # Your Twilio Verified Number

MY_EMAIL = "abc123@mail.com"
MY_PASSWORD = "123456" # Change this to your password
EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"

class NotificationManager:
    '''This class is responsible for sending notifications with the deal flight details.'''

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        '''This method is responsible for sending messages with the deal flight details.'''
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
        
    def send_emails(self, emails, message, google_flight_link):
        '''This method is responsible for sending emails with the deal flight details.'''
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS,587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(MY_EMAIL, MY_PASSWORD)
            smtp.sendmail(MY_EMAIL, emails, f"Subject:Low Price Alert!\n\n{message}\n{google_flight_link}") 
            smtp.quit()
            