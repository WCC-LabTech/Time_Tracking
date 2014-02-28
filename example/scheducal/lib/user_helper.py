from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group
from django.utils import simplejson

def user_dict(user):
    groups = [group.pk for group in user.groups.all()]
    return {
        'id': user.pk,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'groups': groups or None,
        'email': user.email,
    }
@csrf_exempt
@require_http_methods(['POST'])
def modify_user(user):
	
    if User().objects.get(all).filter(user.POST['pk']).exists():
	   updated_user = user
           updated_user.username = user.POST['username']
           updated_user.first_name = user.POST['first_name']
           updated_user.last_name = user.POST['last_name']
           updated_user.email = user.POST['email']
           grp = list(json.loads(user.POST['groups']))
           update_user.save()
           for new_group in Group.objects.all():
               for user_group in grp:
                   if int(new_group.pk) == int(user_group):
                      new_group.user_set.add(update_user)
    else:
	new_user = User()
        new_user.user_name = user.POST['user_name']
        new_user.first_name = user.POST['first_name']
        new_user.last_name = user.POST['last_name']
        new_user.save() 
        for new_group in Group.objects.all():
            for user_group in grp:
                if int(new_group.pk) == int(user_group):
                    new_group.user_set.add(new_user)

@csrf_exempt
@require_http_methods(['POST'])        
def check_clocked_in(request):
	clocked_in = request.POST['clocked_in']
	if clocked_in == "True" or clocked_in == "true" or clocked_in == True :
           return True	
        return False
