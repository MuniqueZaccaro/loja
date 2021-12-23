# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Produto, Venda

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'descricao', 'valor', 'quantidade', 'get_imagem'

    def get_imagem(self, obj):
        return mark_safe('<img src="/{}" width="80px;"></a>'.format(obj.imagem))

    get_imagem.short_description = 'Imagem'

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = 'funcionario', 'cliente', 'produto', 'valor', 'data_entrega',

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name__in=('Funcionario')).exists():
            return qs
        return qs.filter(cliente=request.user)
