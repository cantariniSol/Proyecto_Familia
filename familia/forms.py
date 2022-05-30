
from django import forms
from .models import Familia
class FamiliaForm(forms.ModelForm):
#La clase Meta le dice al formulario que es la clase FamiliaForms cómo comportarse
    class Meta:
        model = Familia
        #fields = ['id', 'nombre', 'apellido', 'fecha_nacimiento', 'edad', 'email', 'telefono', 'direccion', 'imagen']
        fields = '__all__'
        
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'fecha_nacimiento': 'Fecha nacimiento',
            'edad': 'Edad',
            'email': 'Email',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'imagen': 'Imagen'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'fecha_nacimiento': forms.DateInput(attrs={'placeholder': 'Fecha nacimiento'}),
            'edad': forms.TextInput(attrs={'placeholder': 'Edad'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección'}),
        }