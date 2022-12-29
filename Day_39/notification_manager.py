from twilio.rest import Client

TWILIO_SID = "TWILIO_SID"  # Your Twilio SID
TWILIO_AUTH_TOKEN = "TWILIO_AUTH_TOKEN"  # Your Twilio Auth Token
TWILIO_VIRTUAL_NUMBER = "+1 12345 67890" # Your Twilio Virtual Number
TWILIO_VERIFIED_NUMBER = "+1 12345 67890" # Your Twilio Verified Number


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