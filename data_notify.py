from urllib.request import urlopen
from bs4 import BeautifulSoup
from send_email import *
import time
import json

# Define range of sensor's value in normal cases
TEMPERATURE_MIN, TEMPERATURE_MAX = 15, 26
HUDMIDITY_MIN, HUDMIDITY_MAX = 40, 50
ACCELERATOR_X, ACCELERATOR_Y, ACCELERATOR_Z = 1, 1, 1

# Define the frequency for update info from Arduino server
TIME = 10

json_format = []

# Define email content for notification
message = """From: Weather in the Gallery team <weather.in.gallery@gmail.com>
To: To Person <luongdiemquynh1998@gmail.com>
Subject: Warning: Abnormal values on Sensor
There are some abnormal values observed from sensor. Please check it out carefully!
"""


def parse_info(message):
    '''Parse sensor values from arduino and save it'''
    while True:
        # Download from URL and decode as UTF-8 text.
        arduino_url = 'http://192.168.0.12/'
        with urlopen( arduino_url) as webpage:
            print("Crawling data from arduino server")
            content = webpage.read().decode()

        # Save to file.
        with open( 'output.html', 'w' ) as output:
            print("Writing to file output")
            output.write( content )
        

        # Get data parsed from web server into JSON format. Check if data is out of range and send notification to user '''
        # Open the parsed html file
        f = open("output.html", "r")
        content = f.read()
        content_list = content.splitlines()
        f.close()

        # Save sensor data under a list of float format [temperature, hudmidity, acceleratorX, acceleratorY, acceleratorZ]
        sensor_values = []
        sensor_values += [float(i) for i in content_list[0][:-1].split(",")]
        print(sensor_values)

        # Convert data into JSON format
        # sensor_data = {"Temperature" : sensor_values[0], "Hudmidity": sensor_values[1], "AcceleratorX": sensor_values[2], "AcceleratorY": sensor_values[3], "AcceleratorZ": sensor_values[4] }
        sensor_data = {"Temperature" : sensor_values[0], "Hudmidity": sensor_values[1], "AcceleratorX": sensor_values[2], "AcceleratorY": sensor_values[0], "AcceleratorZ": sensor_values[1] }
        json_format.append(sensor_data)
        print(json_format)

        # Write data into json file
        with open("data.json", "w") as f:
            f.write(json.dumps(json_format))

        text_message = ""

        # Check if sensor values is abnormal and send a notify email to user
        if (sensor_values[0] < TEMPERATURE_MIN) or (sensor_values[0] > TEMPERATURE_MAX):
            text_message += """Current temperature is out of range """ + str(sensor_values[0]) + "\n"
        if (sensor_values[1] < HUDMIDITY_MIN) or (sensor_values[1] > HUDMIDITY_MAX):
            text_message += """Current hudmidy is out of range """ + str(sensor_values[1]) + "\n"
        #if (sensor_values[2] < ACCELERATOR_X) or (sensor_values[3] > ACCELERATOR_Y) or (sensor_values[4] > ACCELERATOR_Z):
        #    text_message += """Current accelerator is too low """ + str(sensor_values[2]) + "," + str(sensor_values[3]) + ","  + str(sensor_values[4]) + "\n"
        
        message += text_message


        if len(text_message) != 0:
            print(message)
            send_email(message)

        time.sleep(TIME)

parse_info(message)
