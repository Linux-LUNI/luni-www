from django.http import HttpResponse
from django.db.models import get_model
from django.template.loader import get_template
from django.template.loader import render_to_string


def Home(request):
    obj = render_to_string('home.html')
    return HttpResponse(obj)

def Calendar(request):
    obj = render_to_string('calendar.html')
    return HttpResponse(obj)

def ContactUs(request):
    html = render_to_string('contactus.html')
    return HttpResponse(html )

def Organizations(request):
    html = render_to_string('orgs.html')
    return HttpResponse(html)

