import requests
from requests.auth import HTTPBasicAuth
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
###################################################
fromaddr = "XXXXXXXXXXXXXXXX"
password = "XXXXXXXXXXXXXXXX"
toaddr = "XXXXXXXXXXXXXXXX"
msg = MIMEMultipart()
###################################################

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
################### QA################################
response = requests.get(
  'https://XXXXXX/qa/feed', headers=headers,
  auth=HTTPBasicAuth('XXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXX'))
# 500 id successful 401 unauthorised
print(response.status_code)

if  response.status_code == 500:
     print(' QA ALIVE')
else:
     print(' QA DEAD')
     msg['From'] = fromaddr
     msg['To'] = toaddr
     msg['Subject'] = " QA API DOWN"
     body = " QA API DOWN"
     msg.attach(MIMEText(body, 'plain'))
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.starttls()
     server.login(fromaddr, password)
     text = msg.as_string()
     server.send_message(msg)
     server.quit()
#####################DEV###############################################
response = requests.get(
  'https://XXXXXX/dev/feed', headers=headers,
  auth=HTTPBasicAuth('XXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXX'))
# 500 id successful 401 unauthorised
print(response.status_code)

if  response.status_code == 500:
     print('DEV ALIVE')
else:
     print(' DEV DEAD')
     msg['From'] = fromaddr
     msg['To'] = toaddr
     msg['Subject'] = "DEV API DOWN"
     body1 = "DEV API DOWN"
     msg.attach(MIMEText(body1, 'plain'))
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.starttls()
     server.login(fromaddr, password)
     text = msg.as_string()
     server.send_message(msg)
     server.quit()