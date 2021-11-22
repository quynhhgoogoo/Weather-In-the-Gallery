from urllib.request import urlopen
from bs4 import BeautifulSoup

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