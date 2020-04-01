from home.models import *
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
import json
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
        except Exception as e:
            print (e)

        return render(request, 'home/index.html', {"code":201, "message": "contact_list_updated"})

    return HttpResponse(json.dumps(default_response(status={"code": 404, "message": "request_not_found"}, data={})))
