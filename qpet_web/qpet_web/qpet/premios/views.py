from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,"premios/index.html",{})


def listaPremios(request):
	return render(request,"premios/listaPremios.html",{})


def premio(request):
	return render(request,"premios/premio.html",{})
