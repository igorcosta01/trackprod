# Generated by Django 5.1.1 on 2024-11-19 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0010_alter_produto_cor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='cartucho',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='codigo_barra',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='codigo_barra_pct',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='peso_brt_caixa',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='peso_liq_caixa',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='qtd_total_caixa',
        ),
    ]
