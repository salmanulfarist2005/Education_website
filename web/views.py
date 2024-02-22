from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Teachers,Classes,Blog

# Create your views here.
def index(request):
    context={
        'Teac' : Teachers.objects.all(),
        'class' : Classes.objects.all(),
        'blo' : Blog.objects.all()
    }
    return render(request ,'web/index.html',context)

def contact(request):
    return render(request ,'web/contact.html')



