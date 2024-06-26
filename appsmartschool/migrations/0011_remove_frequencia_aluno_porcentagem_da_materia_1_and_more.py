# Generated by Django 5.0.3 on 2024-04-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartschool', '0010_alter_frequencia_aluno_matricula_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frequencia_aluno',
            name='porcentagem_da_materia_1',
        ),
        migrations.RemoveField(
            model_name='frequencia_aluno',
            name='porcentagem_da_materia_2',
        ),
        migrations.RemoveField(
            model_name='frequencia_aluno',
            name='porcentagem_da_materia_3',
        ),
        migrations.RemoveField(
            model_name='frequencia_aluno',
            name='porcentagem_da_materia_4',
        ),
        migrations.AddField(
            model_name='frequencia_aluno',
            name='aulas_da_materia_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frequencia_aluno',
            name='aulas_da_materia_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frequencia_aluno',
            name='aulas_da_materia_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frequencia_aluno',
            name='aulas_da_materia_4',
            field=models.IntegerField(default=0),
        ),
    ]
