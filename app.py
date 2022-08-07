#!/usr/bin/python3
from netmiko import ConnectHandler
import re,sys
import requests
from flask import *

########################
app = Flask(__name__)

app.route('/maclookup')
def LOOKUPMAC():
    mac = request.args.get('mac', None)
    token=('01g9qj7ta0x1ws7gjr85024hz201g9qj8dnf27p8cx5f36d5cf1wy0ol7xs3gvvu')
    response = requests.get(f'https://api.maclookup.app/v2/macs/{mac}/company/name?apiKey={token}')
    return(response.text)



@app.route('/show_ip_arp')
def show_ip_arp():
    IP = request.args.get('IP', None)
    os = request.args.get('os', None)
    user = request.args.get('user', None)
    passwd = request.args.get('passwd', None)
    return(f'This is a test for {IP} -- {os} -- {user} -- {passwd}')
    



if __name__ == '__main__':
    app.run(host='0.0.0.0')    

