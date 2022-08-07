# proxy_cisco_show
This is a Docker App for proxing cisco show commands to return API output using Netmiko and Textfsm


How to use 
Clone the repo
```
"git clone https://github.com/viperbmw/proxy_cisco_show.git"
"cd proxy_cisco_show"
```
Setup Docker
```
"docker build -t proxy_cisco_show ."
"docker run -d -p 5000:5000 proxy_cisco_show"
```
