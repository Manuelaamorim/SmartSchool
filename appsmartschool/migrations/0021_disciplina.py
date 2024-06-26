# Generated by Django 5.0.3 on 2024-04-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartschool', '0020_remove_notas_media_materia1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, unique=True)),
                ('nome', models.CharField(max_length=40)),
                ('carga_horaria', models.PositiveSmallIntegerField()),
                ('ementa', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
    ]
