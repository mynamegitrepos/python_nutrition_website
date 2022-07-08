from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cadastro(request):
    # Iniciamos com o HttpResponse e depois substituimos pelo render página html.
    # Comentei o HttpResponse para saber iniciar a titulo de teste.
    # return HttpResponse('Voce está na página de cadastro') 
    if request.method == "GET":
      return render(request, 'cadastro.html')
    elif request.method == "POST":
      username = request.POST.get('usuario')
      senha = request.POST.get('senha')
      email = request.POST.get('email')
      confirmar_senha = request.POST.get('confirmar_senha')
      # return HttpResponse('Você está na página de cadastro') 
      return HttpResponse(confirmar_senha)

def logar(request):
  return HttpResponse('Você está na página de login')
