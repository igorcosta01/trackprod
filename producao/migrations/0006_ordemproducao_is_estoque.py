# Generated by Django 5.1.1 on 2024-12-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0005_alter_ordemproducao_quantidade_produzida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemproducao',
            name='is_estoque',
            field=models.BooleanField(default=0),
        ),
    ]
