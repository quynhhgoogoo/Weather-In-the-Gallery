import json
import random
import time
import os
from datetime import datetime
#from data_notify import *

from flask import Flask, Response, render_template,request,redirect,url_for
application = Flask(__name__)
random.seed()  # Initialize the random number generator

# Define email content for notification
message = """From: Weather in the Gallery team <weather.in.gallery@gmail.com>
To: To Person <luongdiemquynh1998@gmail.com>
Subject: Warning: Abnormal values on Sensor
There are some abnormal values observed from sensor. Please check it out carefully!
"""


@application.route('/')
def landing():
    return render_template('index.html')

@application.route('/temperature')
def temperature():
    return render_template('temperature.html')

@application.route('/hudmidity')
def hudmidity():
    return render_template('hudmidity.html')

@application.route('/bulgarydetection')
def accelerator():
    return render_template('bulgarydetection.html')


@application.route('/temperature-data',methods=['GET','POST'])            
def userdata():
    def update_json_data():                                         
            data=[]
            with open("data.json", "r") as sensor_data:
                sensor_data = json.load(sensor_data)
            for temperature in sensor_data:
                temperature = temperature["Temperature"]
                temperature_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': temperature})
            yield f"data:{temperature_data}\n\n"
            time.sleep(1)
    return Response(update_json_data(), mimetype='text/event-stream')


@application.route('/hudmidity-data',methods=['GET','POST'])            
def hudmiditydata():
    def update_json_data():                                         
            data=[]
            with open("data.json", "r") as sensor_data:
                sensor_data = json.load(sensor_data)
            for hudmidity in sensor_data:
                hudmidity = hudmidity["Hudmidity"]
                hudmidity_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': hudmidity})
            yield f"data:{hudmidity_data}\n\n"
            time.sleep(1)
    return Response(update_json_data(), mimetype='text/event-stream')


@application.route('/bulgarydetection-data',methods=['GET','POST'])            
def acceleratordata():
    def update_json_data():                                         
            data=[]
            with open("data.json", "r") as sensor_data:
                sensor_data = json.load(sensor_data)
            for accelerator in sensor_data:
                accelerator = accelerator["Accelerator"]
                accelerator_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': accelerator})
            yield f"data:{accelerator_data}\n\n"
            time.sleep(1)
    return Response(update_json_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    application.run(host = "0.0.0.0", debug=True, threaded=True)
    