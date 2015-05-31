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

# Vista donaciones
def donaciones(request):
    return render(request, "donaciones.html")

# Vista acepto la donacion
def donacion_acepto(request):
    return render(request, "donacion_acepto.html")

# Menus una vez aceptada la donacion
def weapons(request):
    lista = ("Weapons" , "Jewelry", "Shields", "Tattoo", "Others")
    return render(request, "d_info/weapons.html", {"lista_categoria": lista})

# Vista contacto
def contacto(request):
    return render(request, "contacto.html")