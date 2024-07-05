from django import forms 
from django.forms import ModelForm, Form 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import Categoria, Producto, Bodega, Perfil

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion':forms.Textarea(),
            'imagen': forms.FileInput(attrs={'class': 'd-none'})        
        }
        labels ={
                'nombre': 'Nombre',
                'descuento_subscriptor': 'Suscriptor(%)',
                'descuento_oferta': 'Oferta(%)',
        }

class BodegaForm(Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')
    producto = forms.ModelChoiceField(queryset=Producto.objects.none(), label='Producto')
    cantidad = forms.IntegerField(label='Cantidad')
    class Meta:
        fields = '__all__'

class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label='Cuenta')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    class Meta:
        fields = ['username','password'] 

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class RegistroPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'

class UsuarioForm(ModelForm):
   class Meta:
        model = User
        fields = '__all__'

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'         

class BodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'                