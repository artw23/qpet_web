from django.conf import settings
from django.core.mail.message import EmailMessage
from django.shortcuts import render
from .forms import ContactoForm
from django.template.loader import render_to_string
import datetime

# Create your views here.

def contacto(request):
    form = ContactoForm(request.POST or None)
    
    if form.is_valid():
        nombre = form.cleaned_data.get("nombre_completo")
        correo = form.cleaned_data.get("email")
        mensaje = form.cleaned_data.get("mensaje")
        fecha =  datetime.datetime.now()

        
        titulo = "Contacto Qpet"
        
        contenido = render_to_string('mails/contacto-mail.html', {'nombre':nombre,
                                                              'correo':correo,
                                                              'mensaje': mensaje,
                                                                 'fecha':fecha}) # ...

        
        email = EmailMessage(titulo, contenido, settings.EMAIL_HOST_USER,
            ['arturorf23@hotmail.com'], ['A01202457@itesm.mx'])
        email.content_subtype = "html"
        email.send()

        form = ContactoForm()
    
    context = {
        "form": form,
    }
    return render(request,"sitio/contacto.html",context)
