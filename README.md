# proxy_cisco_show
This is a Docker App for proxing cisco show commands to return API output using Netmiko and Textfsm

> Output is in json format only!!!!!!!


## How to setup 
Clone the repo
```
"git clone https://github.com/viperbmw/proxy_cisco_show.git"
"cd proxy_cisco_show"
```
### Setup Docker
```
"docker build -t proxy_cisco_show ."
"docker run -d -p 5000:5000 proxy_cisco_show"
```


## How to use

The script opens port 5000 from the docker container mapped to the host
simply open a webbrower to 
```
http://{localhost}:5000/[show_ip_arp]|[show_mac_addr]?IP=XXX&user=XXX&passwd=XXX&os=XXXX
```
### Example
```
http://serverip:5000/show_ip_arp?IP=10.99.0.1&user=testuser&passwd=p234ssword&os=cisco_ios
```
### Defaults
- os = cisco_ios

All other var's are required and no defaults they can be setup staticly in the app.py file
