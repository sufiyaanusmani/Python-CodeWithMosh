from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Sufiyaan Usmani"
message["to"] = "suffiyaanusmani@gmail.com"
message["subject"] = "Sample Email"

message.attach(MIMEText("Hello World"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login("fastnucesbank@gmail.com", "Hehe.123456")
    smtp.send_message(message)
    print("Sent...")