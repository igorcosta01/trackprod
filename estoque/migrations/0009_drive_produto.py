# Generated by Django 5.1.1 on 2024-12-26 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0011_remove_produto_cartucho_remove_produto_codigo_barra_and_more'),
        ('estoque', '0008_alter_produtoacabado_qtd_total_caixa_drive'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.produto'),
        ),
    ]
