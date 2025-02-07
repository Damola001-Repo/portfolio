import smtplib
# import  ssl
import os


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "damolabalogun79@gmail.com"
    password = os.getenv('PASSWORD')
    receiver = "damolabalogun79@gmail.com"
    # my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == '__main__':
    my_message = """\
Subject: Hi!
How are you doing?
Bye!
    """
    send_mail(my_message)