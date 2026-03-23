import smtplib, sys
from email.message import EmailMessage

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'hereiskaushal@gmail.com'
    msg['To'] = 'hereiskaushal@gmail.com'

    # Connect to Gmail SMTP
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('hereiskaushal@gmail.com', 'umrg vfcg tdii fovp')
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    send_email(sys.argv[1], sys.argv[2])
