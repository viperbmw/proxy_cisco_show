import time
import netmiko
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return ('Hello World! I have been seen {input} times.')
