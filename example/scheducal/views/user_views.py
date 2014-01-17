from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from scheducal.lib.user_helper import user_dict
from django.contrib.auth.models import Group 
import json

@require_http_methods(['GET'])
def user_list(request):
    users = User.objects.all()
    data = [user_dict(user) for user in users]
    data = simplejson.dumps(data)
    return HttpResponse(data, mimetype='application/json')

@require_http_methods(['GET'])
def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    data = simplejson.dumps(user_dict(user))
    return HttpResponse(data, mimetype='application/json')

@csrf_exempt    
@require_http_methods(['POST'])
def delete_user(user_id):
    user = User.objects.all().filter(pk=user_id.POST['pk'])
    status_code = ""
    try:
       user.delete()
       status_code = "201"
    except:
       status_code = "400" 
    return HttpResponse(status_code)
@csrf_exempt
@require_http_methods(['POST'])
def create_user(user):
        
    status_code =""
    new_user = User()
    
    try:
        new_user.username = user.POST['username']
        new_user.first_name = user.POST['first_name']
        new_user.last_name = user.POST['last_name']
        new_user.email = user.POST['email']
        grp = list(json.loads(user.POST['groups']))
        new_user.save()
        for new_group in Group.objects.all():
            for user_group in grp:
                if int(new_group.pk) == int(user_group):
                   new_group.user_set.add(new_user)
        status_code = "201"
    except:
       status_code = "401"
    return HttpResponse(status_code)
@csrf_exempt
@require_http_methods(['POST'])
def update_user(user):
	status_code = "" # default to null string
	updated_user = User().objects(all).filter(pk=user.POST['pk'])
	try:
	   modify_user(user)
	   status_code = "201"
	except:
	   status_code = "401" 
	return HttpResponse(status_code)
# One function to rule them all
@csrf_exempt
@require_http_methods(['POST'])
def update_or_create_user(user):
	status_code = ""
	try:
		modify_user(user)
		status_code = "201" # it was a good call
	except:
		status_code = "401" # something bad happened   
	return HttpResponse(status_code)

