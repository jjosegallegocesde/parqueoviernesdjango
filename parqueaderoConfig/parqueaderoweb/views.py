from django.forms import modelform_factory
from django.shortcuts import render

from parqueaderoweb.models import Tarifas

# Create your views here.


def home(request):

    tarifas=Tarifas.objects.all()

    data={
        'tarifas':tarifas
    }

    return render (request,'index.html',data)

def conductor(request):
    return render (request,'conductor.html')

def registro(request):
    return render (request,'registroTicket.html')
    
