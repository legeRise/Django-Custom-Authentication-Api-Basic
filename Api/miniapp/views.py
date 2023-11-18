from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from .models import Information
from django.views.decorators.csrf import csrf_exempt
import json
import re

@csrf_exempt
def signup(request):

    if request.method == 'POST':
        data = json.loads(request.body)

        username = data.get('username')
        password = data.get('password')
        confirm = data.get('confirm')
        
        # check if user already exists
        check_user = Information.objects.filter(username=username)

        if check_user.exists():
            return HttpResponseBadRequest(json.dumps({'message': 'User Already Exists'}), content_type='application/json')

        elif len(username) < 5:
            return HttpResponseBadRequest(json.dumps({'message': 'Username must be at least 5 characters'}), content_type='application/json')

        elif not re.search(r'\d', username):
            return HttpResponseBadRequest(json.dumps({'message': 'Username must contain a number'}), content_type='application/json')

        elif password != confirm:
            return HttpResponseBadRequest(json.dumps({'message': 'Password and Confirm Password should be the same'}), content_type='application/json')

        elif len(password) < 5:
            return HttpResponseBadRequest(json.dumps({'message': 'Password should contain at least 5 characters'}), content_type='application/json')

        elif " " in username:
            return HttpResponseBadRequest(json.dumps({'message': 'username should not contain any space'}), content_type='application/json')

        elif " " in password:
            return HttpResponseBadRequest(json.dumps({'message': 'password should not contain any space'}), content_type='application/json')

        else:
            # If everything is fine, Sign Up the user
            user = Information(username=username, password=password, confirm=confirm)
            user.save()
            return JsonResponse({'message': 'Registration Successful'})

    return JsonResponse({'message': 'Only POST Method is Allowed'})

#_____________end____________


@csrf_exempt
def login(request):

    if request.method == 'POST':
        data = json.loads(request.body)

        username = data.get('username')
        password = data.get('password') 

        # authenticate user before logging in 
        check_user = Information.objects.filter(username=username, password=password)

        if check_user.exists():
            return JsonResponse({'message': 'Login Successful'})
        else:   
            return HttpResponseBadRequest(json.dumps({'message': 'Invalid Username or Password'}), content_type='application/json')

    return JsonResponse({'message': 'Only POST Method is Allowed'})

#_____________end____________