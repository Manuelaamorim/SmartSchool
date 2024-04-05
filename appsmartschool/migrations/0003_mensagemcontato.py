# Generated by Django 5.0.3 on 2024-04-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartschool', '0002_dados_saude_alter_useraluno_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensagemContato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('mensagem', models.TextField(max_length=500)),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]