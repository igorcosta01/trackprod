# Generated by Django 5.1.1 on 2024-12-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0007_produtoacabado_cartucho_produtoacabado_codigo_barra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoacabado',
            name='qtd_total_caixa',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(choices=[('A', 'Rua A'), ('B', 'Rua B'), ('C', 'Rua C')], max_length=1)),
                ('numero', models.PositiveIntegerField()),
                ('ocupado', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('rua', 'numero')},
            },
        ),
    ]
