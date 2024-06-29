from django import forms 
from django.forms import ModelForm, Form 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import Categoria, Producto, Bodega, Perfil

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '_all_'
        widgets = {
            'descripcion':forms.Textarea(),
            'imagen': forms.FileInput(attrs={'class': 'd-none'})        
        }
        labels ={
                'nombre': 'Nombre',
                'descuento_subscriptor': 'Suscriptor(%)',
                'descuento_oferta': 'Oferta(%)',
        }

class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label='Cuenta')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    class Meta:
        fields = ['username','password'] 
            