# Generated by Django 3.2.9 on 2021-12-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20211221_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='data_entrega',
            field=models.DateField(null=True, verbose_name='Data da Entrega'),
        ),
    ]
