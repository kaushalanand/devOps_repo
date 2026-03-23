import smtplib, sys
from email.message import EmailMessage

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'hereiskaushal@gmail.com'
    msg['To'] = 'hereiskaushal@gmail.com'

    try:
        # Connect to Gmail SMTP
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # Note: I removed the spaces from your password below
        server.login('hereiskaushal@gmail.com', 'umrgvfcgtdiifovp')
        server.send_message(msg)
        server.quit()
        print("Successfully sent email!")
    except Exception as e:
        print(f"Error: Could not send email. {e}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        send_email(sys.argv[1], sys.argv[2])
    else:
        print("Missing arguments. Usage: python3 script.py <subject> <body>")
