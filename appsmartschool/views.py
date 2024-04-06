from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserAluno
from .models import Dados_saude
from .models import MensagemContato
from .models import Frequencia_Aluno
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login_view(request):
    if request.method == "POST":
        cpf = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=cpf, password=senha)
        if user is not None:
            login(request, user)
            return redirect('appsmartschool:pagina_home')  # Substitua pelo nome da URL para redirecionar após o login
        else:
            messages.error(request, 'CPF ou senha inválidos.')
    return render(request, 'appsmartschool/login.html')

@login_required
def dados_saude_visualizar(request):

    try:
        dados = Dados_saude.objects.all()
    except Dados_saude.DoesNotExist:
        messages.error(request, 'Dados de saúde não cadastrados.')

    return render(request, 'appsmartschool/dados_saude.html', {"dados":dados})
        #precisa criar um novo html?

@login_required
def frequencia_alunos_visualizar(request):

    try:
        frequencias = Frequencia_Aluno.objects.all()
    except Frequencia_Aluno.DoesNotExist:
        messages.error(request, 'Frequência não cadastrada.')

    return render(request, 'appsmartschool/frequencia.html', {"frequencias": frequencias})

@login_required
def formulario_contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')

        MensagemContato.objects.create(nome=nome, email=email, telefone=telefone, mensagem=mensagem)

        # Após salvar os dados, redirecione para uma página de sucesso
        return redirect('appsmartschool:contato_sucesso')

    return render(request, 'appsmartschool/formulario_contato.html')

@login_required
def contato_sucesso(request):
    return render(request, 'appsmartschool/contato_sucesso.html')

@login_required
def home(request):
    return render(request, 'appsmartschool/home.html')

@login_required
def logout_view(request):
    logout(request)
    # Redireciona para a página de login, ou outra página que desejar
    return redirect('appsmartschool:login')
