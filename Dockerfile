FROM python:3
WORKDIR /proxy_cisco_show
ENV FLASK_APP=app.py
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./app.py" ]
