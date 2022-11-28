import django.contrib.auth
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def index(request):
    if request.user.is_authenticated:
        django.contrib.auth.logout(request)
        return HttpResponse(f"<h1>Your unique code is: <strong>{generate_random_string(4)}</strong></h1><br><h1>Reload page to get a new code</h1>")
    else:
        return HttpResponse('<a href="/login"><h1>You need to login</h1></a>')
# Create your views here.
