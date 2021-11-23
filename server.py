from urllib.request import urlopen
from bs4 import BeautifulSoup
from send_email import *


# Define range of sensor's value in normal cases
TEMPERATURE_MIN, TEMPERATURE_MAX = 15, 26
HUDMIDITY_MIN, HUDMIDITY_MAX = 40, 50
ACCELERATOR_X, ACCELERATOR_Y, ACCELERATOR_Z = 1, 1, 1


'''
# Download from URL and decode as UTF-8 text.
arduino_url = 'http://192.168.43.138/'
with urlopen( arduino_url) as webpage:
    content = webpage.read().decode()

# Save to file.
with open( 'output.html', 'w' ) as output:
    output.write( content )
'''

# Open the parsed html file
f = open("output.html", "r")
content = f.read()
content_list = content.splitlines()
f.close()

# Save sensor data under a list of float format [temperature, hudmidity, acceleratorX, acceleratorY, acceleratorZ]
sensor_values = content_list[0][:-1].split(",")
sensor_values = [float(i) for i in sensor_values]
print(sensor_values)

# Check if sensor values is abnormal and send a notify email to user
message = """From: Weather in the Gallery team <weather.in.gallery@gmail.com>
To: To Person <luongdiemquynh1998@gmail.com>
Subject: Warning: Abnormal values on Sensor
There are some abnormal values observed from sensor. Please check it out carefully!
"""

if (sensor_values[0] < TEMPERATURE_MIN) or (sensor_values[0] > TEMPERATURE_MAX):
    message += """Current temperature is out of range """ + str(sensor_values[0]) + "\n"
if (sensor_values[1] < HUDMIDITY_MIN) or (sensor_values[1] > HUDMIDITY_MAX):
    message += """Current hudmidy is out of range """ + str(sensor_values[1]) + "\n"
if (sensor_values[2] < ACCELERATOR_X) or (sensor_values[3] > ACCELERATOR_Y) or (sensor_values[4] > ACCELERATOR_Z):
    message += """Current accelerator is too low """ + str(sensor_values[2]) + "," + str(sensor_values[3]) + ","  + str(sensor_values[4]) + "\n"

if len(message) != 0:
    send_email(message)