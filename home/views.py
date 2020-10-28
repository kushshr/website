from home.models import *
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
import smtplib, email
import datetime
import pytz
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from django.contrib.auth import authenticate, login

def default_response(status={},data={}):
    if status:
        return {'status':status,'response':data}
    else:
        return {'status':status,'response':data}

@csrf_exempt
def contact(request):
    if request.method =='POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email","")
        message = request.POST.get("message","")
        print (request.POST)
        if not name or not email:
            return render(request, 'home/index.html', {"code": 401, "message": "mandatory_fields_missing"})
        try:
            contact = Contacts()
            contact.name = name
            contact.email = email
            contact.message = message
            contact.save()

            mail_message_body = str(name) + """(""" + str(email) + """) """ + """has requeted to get in touch with the TOMP Working Group. Here's their message: """ + str(message)

            send_email("", "", "Contact Request", mail_message_body)
            
        except Exception as e:
            print (e)

        return render(request, 'home/index.html', {"code": 201, "message": "Done"})

    return HttpResponse(json.dumps(default_response(status={"code": 404, "message": "method_not_allowed"}, data={})))


def send_email(recipient, cc, subject, message):
    tz = pytz.timezone("Europe/Amsterdam")

    username = "kushagrasharma.ece09@gmail.com"
    password = ""

    msg = MIMEMultipart()
    msg['From'] = "kushagrasharma.ece09@gmail.com"
    msg['To'] = recipient
    msg['Cc'] = cc
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    completeList = cc.split(",") + [recipient]

    # part = MIMEBase('application', "octet-stream")
    # part.set_payload(open(filename, "rb").read())
    # encode_base64(part)

    # part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(filename))

    # msg.attach(part)

    try:
        mailServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        mailServer.ehlo()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, completeList, msg.as_string())
        mailServer.close()

    except Exception as e:
        print("{time: " + datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S") + ", message: " + str(e) + "}")