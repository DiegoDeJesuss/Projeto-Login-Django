from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
# Create your views here.
def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request,'cadastro.html', {'status': status})
    



def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')



    if len(nome.strip()) == 0 or  len(email.strip()) == 0: # se o nome ou e-mail vazio redireciona para pagina login.
        return redirect('/auth/cadastro?status=1')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro?status=2')
    
    usuario = Usuario.objects.filter(email = email) #verifica se já tem um usuario com esse e-mail

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest() #criptografa senha
        usuario = Usuario(nome = nome,
                            senha = senha,
                            email = email)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
        
        
    except:
        return redirect('/auth/cadastro/?status=4')
    

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest() #criptografa senha
    
    usuario = Usuario.objects.filter(email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) >0:
        pass



