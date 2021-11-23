#!/usr/bin/python3

import smtplib


def send_email(message):
    ''' Send an email to user when abnormal activities is detected '''
    
    sender = 'weather.in.gallery@gmail.com'
    receiver = 'luongdiemquynh1998@gmail.com'
    password= "weatherinthegallery"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    print("Login suceed!")

    server.sendmail(sender, receiver, message)
    print("Email has sent to", receiver)
    print(message)
