from twilio.rest import Client
import smtplib

TWILIO_SID = "AC11232d0bc07915f66079ef47db11bb7c"
TWILIO_AUTH_TOKEN = "a0107821cfcbdf0d68683866d1e8ebae"
TWILIO_VIRTUAL_NUMBER = "+13253356165"
TWILIO_VERIFIED_NUMBER = "+917306231273"

MY_EMAIL = "amaljalappatttest@gmail.com"
PASSWORD = "Super*123"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                                    )
