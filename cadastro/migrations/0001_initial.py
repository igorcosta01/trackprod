# Generated by Django 5.1.1 on 2024-09-26 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_funcionario', models.CharField(max_length=100)),
                ('matricula_funcionario', models.CharField(max_length=5)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('descricao', models.TextField(blank=True)),
                ('material', models.CharField(max_length=100)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade_medida', models.CharField(max_length=50)),
                ('abreviacao', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=4, unique=True)),
                ('descricao', models.TextField(blank=True)),
                ('quantidade_estoque', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unidade_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.unidademedida')),
            ],
            options={
                'verbose_name_plural': 'Materiais',
            },
        ),
    ]
