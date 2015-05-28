from django.http import HttpResponse, Http404
import datetime

# Vista Hola
def hola(request):
    return HttpResponse("Hola mundo")

# Vista de fecha y hora actual
def fecha_actual(request):
    ahora = datetime.datetime.now()
    html = "<html><body><h1>Fecha:</h1><h3>%s</h3><body></html>" % ahora
    return HttpResponse(html)

# Vista de fecha con horas adelantadas
def horas_adelante(request, pHoras):
    try:
        pHoras = int(pHoras)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours = pHoras)
    html = "<html><body><h1>En %s horas, seran las </h1><br><hr>%s</html></body>" % (pHoras, dt)
    return HttpResponse(html)

# Vista que suma un numero mas 5
def suma(request, pNumero):
    try: #Evalua la(s) linea(s) dentadas dentro del try
        pNumero = int(pNumero) #Se convierte la cadena en numero
    except ValueError: #Al no cumplirse o encontrar un problema lanzara un error
        raise Http404() # Lanza la pagina 404 --> Conocida como error comunmente
    valor_suma = pNumero + 5 #Suma el numero en 5 mas
    html = "<html><body>La suma es %s</body></html>" % valor_suma
    return HttpResponse(html)