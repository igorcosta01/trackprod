# Generated by Django 5.1.1 on 2024-12-26 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0011_remove_produto_cartucho_remove_produto_codigo_barra_and_more'),
        ('estoque', '0009_drive_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='produto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.produto'),
        ),
    ]
