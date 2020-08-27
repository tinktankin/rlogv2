from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def mandate(request):
    return render(request,'mandate_html.html');

