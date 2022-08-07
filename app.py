#!/usr/bin/python3
from netmiko import ConnectHandler
import re,sys,os
import requests
from flask import *

########################
app = Flask(__name__)

@app.route('/show_ip_arp')
def show_ip_arp():
    IP = request.args.get('IP', None)
    os = request.args.get('os', 'cisco_ios')
    user = request.args.get('user', 'autobot')
    passwd = request.args.get('passwd', 'WSX@#$rdx567-Prime')
    net_connect=ConnectHandler(device_type=os, ip=IP, username=user, password=passwd)
    showarp=net_connect.send_command("show ip arp",use_textfsm=True)
    return(showarp)
    
@app.route('/show_mac_addr')
def show_mac_addr():
    IP = request.args.get('IP', None)
    os = request.args.get('os', 'cisco_ios')
    user = request.args.get('user', 'autobot')
    passwd = request.args.get('passwd', 'WSX@#$rdx567-Prime')
    net_connect=ConnectHandler(device_type=os, ip=IP, username=user, password=passwd)
    net_connect.send_command("term len 0")
    showmac=net_connect.send_command("show mac address-table",use_textfsm=True)
    return(showmac)


if __name__ == '__main__':
    app.run(host='0.0.0.0')    

