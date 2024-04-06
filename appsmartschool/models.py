from django.db import models
from django.contrib.auth.models import User

class UserAluno (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=200)
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11)
    data_de_nascimento = models.DateField("Created on")
    endereco = models.TextField()
    serie = models.PositiveSmallIntegerField()
    email = models.EmailField()
    nome_responsavel= models.CharField(max_length=200, null=False)
    cpf_responsavel = models.CharField(max_length=11, null=False)
    telefone = models.CharField(max_length=11, null=False)
    email_responsavel = models.EmailField();

    class Meta:
        app_label = 'appsmartschool'

class Dados_saude(models.Model):
    peso = models.FloatField(max_length=4, null=False)
    altura = models.FloatField(max_length = 4, null=False)
    restricao_alimentar = models.TextField(max_length = 100)
    tdah = models.CharField(max_length = 4)
    pcd = models.CharField(max_length = 4)

    class Meta:
        app_label = 'appsmartschool'

class MensagemContato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.PositiveBigIntegerField()
    mensagem = models.TextField(max_length=500)
    data_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'appsmartschool'

class Frequencia_Aluno(models.Model):
    colegio = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    serie = models.PositiveSmallIntegerField()
    matricula = models.CharField(max_length=200)
    materia_1 = models.CharField(max_length=200, null=False)
    faltas_da_materia_1 =  models.PositiveSmallIntegerField(null=False)
    porcentagem_da_materia_1 = models.CharField(max_length=4, null=False)
    materia_2 = models.CharField(max_length=200, null=False)
    faltas_da_materia_2 =  models.PositiveSmallIntegerField(null=False)
    porcentagem_da_materia_2 = models.CharField(max_length=4, null=False)
    materia_3 = models.CharField(max_length=200, null=False)
    faltas_da_materia_3 =  models.PositiveSmallIntegerField(null=False)
    porcentagem_da_materia_3 = models.CharField(max_length=4, null=False)
    materia_4 = models.CharField(max_length=200, null=False)
    faltas_da_materia_4 =  models.PositiveSmallIntegerField(null=False)
    porcentagem_da_materia_4 = models.CharField(max_length=4, null=False)

    class Meta:
        app_label = 'appsmartschool'