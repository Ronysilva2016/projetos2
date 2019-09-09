from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    template_nome='SServices/home.html'
    return render(request,template_nome)
def SysChamada(request):
    template_nome='Chamada/'