from django.shortcuts import render, HttpResponse

# se crean las platillas de la pajina web
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def portafolio(request):
    return render(request,"core/portafolio.html")

def contacto(request):
    return render(request,"core/contacto.html")
    
