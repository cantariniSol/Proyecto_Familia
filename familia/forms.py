from django import forms
from .models import Familia

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        # fields = ['id', 'nombre', 'apellido', 'fecha_nacimiento', 'edad', 'email', 'telefono', 'direccion', 'imagen']
        fields = '__all__'
