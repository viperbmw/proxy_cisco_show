#!/usr/bin/python3
from netmiko import ConnectHandler
import re,sys,os
import requests
from flask import *
#templates = os.path.dirname(os.path.abspath(__file__)) + '/ntc-templates/ntc_templates/templates'
#os.environ['NET_TEXTFSM']= templates

########################
app = Flask(__name__)

@app.route('/show_ip_arp')
def show_ip_arp():
    IP = request.args.get('IP', None)
    os = request.args.get('os', 'cisco_ios')
    user = request.args.get('user', 'autobot')
    passwd = request.args.get('passwd', 'WSX@#$rdx567-Prime')
    net_connect=ConnectHandler(device_type=os, ip=IP, username=user, password=passwd)
    showarp=net_connect.send_command("show ip arp")#,use_textfsm=True)
    return(showarp)
    



if __name__ == '__main__':
    app.run(host='0.0.0.0')    

