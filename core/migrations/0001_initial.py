# Generated by Django 4.1.4 on 2022-12-14 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=1000)),
                ('dt_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=1000)),
                ('descricao', models.CharField(max_length=1000)),
                ('dt_inicio', models.DateField()),
                ('dt_fim', models.DateField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.status')),
            ],
        ),
    ]