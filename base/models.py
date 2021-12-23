# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from datetime import date

import decimal

# Create your models here.

class Produto(models.Model):
    descricao = models.CharField(verbose_name='Descrição', max_length=50)
    valor = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name='Valor')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    imagem = models.ImageField(verbose_name='Imagem', upload_to='produtos', null=True)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.descricao


class Venda(models.Model):
    funcionario = models.ForeignKey(User, verbose_name='Funcionário', on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, verbose_name='Cliente', on_delete=models.CASCADE, related_name='venda_set2', default=1)
    produto = models.ForeignKey(Produto, verbose_name='Produto', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name='Valor')
    data_entrega = models.DateField(verbose_name='Data da Entrega', null=True, blank=True)


    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return '{} - {}'.format(self.id, self.produto)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.data = date.today()
        super().save(*args, **kwargs)
