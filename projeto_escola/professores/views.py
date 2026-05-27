from django.shortcuts import render

# Create your views here.
def lista_profs(request):
    return render(request, 'professores/lista_profs.html')
