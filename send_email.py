#!/usr/bin/python3

import smtplib

sender = 'weather.in.gallery@gmail.com'
receiver = 'luongdiemquynh1998@gmail.com'
password="weatherinthegallery"

message = """From: Weather in the Gallery team <weather.in.gallery@gmail.com>
To: To Person <luongdiemquynh1998@gmail.com>
Subject: Warning: Abnormal values on Sensor

There are some abnormal values observed from sensor. Please check it out carefully!
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print("Login suceed!")

server.sendmail(sender, receiver, message)
print("Email has sent to", receiver)