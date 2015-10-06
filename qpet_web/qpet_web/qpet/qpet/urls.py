"""qpet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$', 'pages.views.home', name="home"),

    url(r'^somos$', 'pages.views.somos', name="somos"),
    url(r'^somos/objetivos$', 'pages.views.objetivos', name="objetivos"),
    url(r'^somos/alianzas$', 'pages.views.alianzas', name="alianzas"),

    url(r'^proyectos$', 'pages.views.proyectos', name="proyectos"),

    url(r'^fondeos$', 'pages.views.fondeos', name="fondeos"),
    url(r'^fondeos/centros_de_acopio$', 'pages.views.centros', name="centros"),

    url(r'^qpetizate$', 'pages.views.qpetizate', name="qpetizate"),
    url(r'^qpetizate/educacion_ambiental$', 'pages.views.educacion_ambiental', name="educacion_ambiental"),
    url(r'^qpetizate/inspectores_ambientales$', 'pages.views.inspectores_ambientales', name="inspectores_ambientales"),
    url(r'^qpetizate/servicio_social$', 'pages.views.servicio_social', name="servicio_social"),
    url(r'^qpetizate/unete$', 'pages.views.unete', name="unete"),
    url(r'^qpetizate/visitas_a_comunidades$', 'pages.views.visitas_comunidades', name="visitas_comunidades"),


    url(r'^premios$', 'premios.views.index', name="premios"),
    
    url(r'^premios/listar-premios$', 'premios.views.listaPremios', name="listar-premios"),
    
    url(r'^premios/ver-premio$', 'premios.views.premio', name="ver-premio"),
    
    
    
    url(r'^contacto$', 'contacto.views.contacto', name="contacto"),
    
    url(r'^iniciar-sesion$', 'login.views.login', name="iniciarSesion"),

    url(r'^admin/', include(admin.site.urls)),
] 

if settings.DEBUG:
	urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    