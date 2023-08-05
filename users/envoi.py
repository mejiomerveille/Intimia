import smtplib
from email.message import EmailMessage

def send_mail(user_code,email):
    gmail_cfg =  {
        "server" : "smtp.gmail.com",
        "port" : "465",
        "email": "intimia805@gmail.com",
        "pwd":"cazhydtdafoknqxe"
    }

    msg = EmailMessage()
    msg["to"] = email
    msg["from"] = gmail_cfg["email"]
    msg["subject"] = "OTP verification"
    msg.set_content(f"Votre code OTP est : {user_code}")

    with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp:
        smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
        smtp.send_message(msg)
        print("Email envoyé !")
# send_mail('guiffopaterne@gmail.com')