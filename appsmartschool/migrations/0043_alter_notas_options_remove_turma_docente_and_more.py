# Generated by Django 5.0.3 on 2024-05-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartschool', '0042_alter_notas_options_alter_notas_disciplina'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notas',
            options={'verbose_name': 'Notas do aluno', 'verbose_name_plural': 'Notas do aluno'},
        ),
        migrations.RemoveField(
            model_name='turma',
            name='docente',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='matricula_docente',
        ),
        migrations.AlterField(
            model_name='notas',
            name='nota1',
            field=models.FloatField(max_length=4),
        ),
        migrations.AlterField(
            model_name='notas',
            name='nota2',
            field=models.FloatField(max_length=4),
        ),
        migrations.AlterField(
            model_name='notas',
            name='nota3',
            field=models.FloatField(max_length=4),
        ),
    ]
