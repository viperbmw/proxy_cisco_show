FROM ubuntu
WORKDIR /proxy_cisco_show
ENV FLASK_APP=app.py
COPY requirements.txt ./
RUN apt-get update && apt-get install -y git wget python3 python3-pip 
RUN pip3 install --no-cache-dir -r requirements.txt
RUN git clone https://github.com/networktocode/ntc-templates.git
RUN export NET_TEXTFSM=/ntc-template/ntc_templates/templates/
COPY . .
#CMD ['bash']
CMD [ "python3", "./app.py" ]
