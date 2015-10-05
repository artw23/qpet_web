from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,"sitio/home.html",{})



def somos(request):
	return render(request,"sitio/somos.html",{})

def objetivos(request):
	return render(request,"sitio/objetivos.html",{})

def alianzas(request):
	return render(request,"sitio/alianza.html",{})



def proyectos(request):
	return render(request,"sitio/proyectos.html",{})




def fondeos(request):
	return render(request,"sitio/fondeos.html",{})

def centros(request):
	return render(request,"sitio/centro_acopio.html",{})


def qpetizate(request):
	return render(request,"sitio/qpetizate.html",{})

def educacion_ambiental(request):
	return render(request,"sitio/educacion_ambiental.html",{})

def inspectores_ambientales(request):
	return render(request,"sitio/inspectores_ambientales.html",{})

def servicio_social(request):
	return render(request,"sitio/servicio_social.html",{})

def unete(request):
	return render(request,"sitio/unete.html",{})

def visitas_comunidades(request):
	return render(request,"sitio/visitas_a_comunidades.html",{})


