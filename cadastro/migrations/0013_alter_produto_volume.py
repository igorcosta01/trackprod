# Generated by Django 5.1.1 on 2025-01-08 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0012_produto_status_alter_produto_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='volume',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
