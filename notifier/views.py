from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def home(request):
    webpush = {"group": "kanishka"}
    return render(request, 'notifier/home.html',  {"webpush": webpush})
