# otp_handler.py
import random
import smtplib
from twilio.rest import Client

class OTPHandler:
    def __init__(self):
        self.otp_store = {}
    
    def generate_otp(self, phone):
        otp = random.randint(100000, 999999)
        self.otp_store[phone] = otp
        # Send via SMS (Twilio) or Email
        self.send_sms(phone, f"Your MPK OTP is: {otp}")
        return otp
    
    def verify_otp(self, phone, otp):
        return self.otp_store.get(phone) == int(otp)
    
    def send_sms(self, to, message):
        # Implement Twilio or other SMS gateway
        pass