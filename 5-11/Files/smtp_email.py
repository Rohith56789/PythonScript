import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    sender_email = "pvrohith00@gmail.com"
    receiver_email = "sonam_skills@pw.live"
    password = "ythe ndao dczl rdin" 
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com', "587") as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

send_email("Task Completed ", "(Thanks Mam)The smtplib is working perfectly.")
