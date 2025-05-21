from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    """
    View function for the web page.
    """
    template = loader.get_template('site_web/index.html')
    return HttpResponse(template.render())
