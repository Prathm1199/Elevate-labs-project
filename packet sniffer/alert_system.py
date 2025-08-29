import smtplib


def log_alert(message):
    with open("alerts.log", "a") as f:
        f.write(message + "\n")
    print("ALERT:", message)


# Optional email alert (requires valid credentials)
def send_email_alert(message):
    sender = "your_email@gmail.com"
    password = "your_app_password"
    recipient = "destination_email@gmail.com"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
    server.quit()
