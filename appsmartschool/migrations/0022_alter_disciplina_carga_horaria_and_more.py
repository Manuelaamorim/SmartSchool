# Generated by Django 5.0.3 on 2024-04-28 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartschool', '0021_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='carga_horaria',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^\\d{1,3}$', 'Somente números são permitidos.')]),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='codigo',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
