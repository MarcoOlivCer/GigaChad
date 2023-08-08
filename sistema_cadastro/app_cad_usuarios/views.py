from django.shortcuts import render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')
    

def usuarios(request):
    
    # Salvar o dados da tela para o banco de dados.
    novo_usuario = Usuario()
    nome = request.POST.get('Nome')
    idade = request.POST.get('Idade')
    novo_usuario.save()
    
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    
    usuarios = {
        'usuarios': Usuario.objects.all()        
    }
    
    #Retornar os dados para a página de listagem de usuarios
    
    return render(request, 'usuarios/home.html', usuarios)