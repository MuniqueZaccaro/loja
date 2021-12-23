# Generated by Django 3.2.9 on 2021-12-20 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='usuario',
            new_name='funcionario',
        ),
        migrations.AddField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='venda_set2', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
