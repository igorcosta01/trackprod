# Generated by Django 5.0.6 on 2024-10-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_remove_funcionario_ativo_funcionario_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=255)),
                ('tipo_cliente', models.CharField(choices=[('pf', 'Pessoa Física'), ('pj', 'Pessoa Jurídica')], default='pf', max_length=2)),
                ('cpf_cnpj', models.CharField(max_length=18, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco', models.TextField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='matricula_funcionario',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]