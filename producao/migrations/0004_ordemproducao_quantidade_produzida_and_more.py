# Generated by Django 5.0.6 on 2024-10-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0003_ordemproducao_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemproducao',
            name='quantidade_produzida',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordemproducao',
            name='saldo_op',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordemproducao',
            name='quantidade',
            field=models.FloatField(),
        ),
    ]
