# Generated by Django 5.1.1 on 2024-11-18 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_produto_capacidade_produto_codigo_barra_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='capacidade',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='dimensao_boca',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='dimensao_fundo',
        ),
    ]
