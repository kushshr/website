from home.models import *
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def default_response(status={},data={},msg='', err = {}):
    if status:
        return {'status':status,'response':data}
    else:
        return {'status':status,'response':data}

@csrf_exempt
def contact(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email","")
    message = request.POST.get("message","")

    if not name or not email:
        return HttpResponse(json.dumps(default_response(status={"code":401, "message": "mandatory_fields_missing"}, data={})))

    try:
        contact = Contacts()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
    except Exception as e:
        print (e)

    return HttpResponse(json.dumps(default_response(status={"code":201, "message": "contact_list_updated"}, data = {})))