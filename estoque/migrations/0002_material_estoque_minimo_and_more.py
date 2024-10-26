# Generated by Django 5.0.6 on 2024-10-24 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='estoque_minimo',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='material',
            name='quantidade_estoque',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
