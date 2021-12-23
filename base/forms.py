from datetime import date, timedelta
from django import forms
from django.contrib.auth.models import User
from base.models import Venda

class RegistrarEntregaForm(forms.Form):
    venda = forms.ModelChoiceField(Venda.objects, label='Venda')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['venda'].queryset = Venda.objects.filter(data_entrega__isnull=True)

    def processar(self):
        venda = self.cleaned_data['venda']
        venda.data_entrega = date.today()
        venda.save()

