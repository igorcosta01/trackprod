# Generated by Django 5.0.6 on 2024-10-28 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_alter_movimentoestoqueacabado_quantidade_movimentada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentoestoqueacabado',
            name='quantidade_movimentada',
            field=models.IntegerField(),
        ),
    ]
