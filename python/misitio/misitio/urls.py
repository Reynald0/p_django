from django.conf.urls import include, url
from django.contrib import admin
from misitio.views import hola, fecha_actual, horas_adelante, suma

urlpatterns = [
    # Examples:
    # url(r'^$', 'misitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hola/$', hola),
    url(r'^fecha/$', fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante),
    url(r'^suma/(\d{1,2})/$', suma),
]
