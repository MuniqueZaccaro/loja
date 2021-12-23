# Generated by Django 3.2.9 on 2021-12-21 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_auto_20211220_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(null=True, upload_to='produtos', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='venda_set2', to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Funcionário'),
        ),
    ]