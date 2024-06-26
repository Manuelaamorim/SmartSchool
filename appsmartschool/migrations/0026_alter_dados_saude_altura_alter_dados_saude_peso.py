# Generated by Django 5.0.4 on 2024-04-29 05:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartschool', '0025_alter_horarioaula_turma_alter_useraluno_turma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_saude',
            name='altura',
            field=models.FloatField(help_text='Altura deve ser entre 0.50 m e 2 m.', max_length=4, validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='dados_saude',
            name='peso',
            field=models.FloatField(help_text='Idade deve ser entre 10 e 120 anos.', max_length=4, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
