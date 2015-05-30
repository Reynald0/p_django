from django.shortcuts import render

# Vista principal
def inicio(request):
    return render(request, "index.html")

# Vista informacion
def informacion(request):
    return render(request, "info.html")

# Vista descargas
def descargas(request):
    return render(request, "descargas.html")

# Vista contacto
def contacto(request):
    return render(request, "contacto.html")