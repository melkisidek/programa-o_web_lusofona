from django import forms
from django.forms import ModelForm
from .models import Post, Tfc


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descricao'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'link'}),
            
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'autor': 'autor',
            'descricao': 'descricao',
            'link': 'link',
        }



class TfcForm(ModelForm):
    class Meta:
        model = Tfc
        fields = '__all__'


       