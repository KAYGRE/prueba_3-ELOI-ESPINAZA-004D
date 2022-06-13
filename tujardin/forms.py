from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget

from .models import Tipo, Producto, cliente


class prodform(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['Id', 'Nombre', 'Precio', 'Tipo']
        labels ={
            'Id': 'Id', 
            'Nombre': 'Nombre', 
            'Precio': 'Precio', 
            'Tipo': 'Tipo',
        }
        widgets={
            'Id': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Id', 
                    'id': 'Id'
                }
            ), 
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'Nombre'
                }
            ), 
            'Precio': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Precio', 
                    'id': 'Precio'
                }
            ), 
            'Tipo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'Tipo',
                }
            )

        }

class clientform(forms.ModelForm):

    class Meta: 
        model= cliente
        fields = [ 'Nombre', 'Gmail']
        labels ={
            'Nombre': 'Nombre', 
            'Gmail': 'Gmail', 
        }
        widgets={
            'Gmail': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Gmail', 
                    'id': 'Gmail'
                }
            ), 
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'Nombre'
                }
            ), 
        }