from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid
from django.shortcuts import redirect
from django.contrib.auth.models import User
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
    if not password_is_valid(request, senha, confirmar_senha):
        return redirect('/auth/cadastro')

        try:
          user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha,
                                            is_active=False)
          user.save()
          return redirect('/auth/logar')
        except:
          return redirect('/auth/cadastro')

def logar(request):
  return HttpResponse('Você está na página de login')
