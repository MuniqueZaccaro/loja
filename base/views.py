# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from base.forms import RegistrarEntregaForm
# Create your views here.

def registrar_entrega(request):
    form = RegistrarEntregaForm(data=request.POST or None)
    if form.is_valid():
        form.processar()
        messages.success(request, 'Entrega registrada com sucesso.')
        return HttpResponseRedirect('/admin/')
    return render(request, 'registrar_entrega.html', dict(form=form))
