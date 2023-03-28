from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ChartsSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Начальная дата")
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Конечная дата")
    kd = forms.ModelChoiceField(queryset=Kind.objects.all(), label="Вид продукции")
    con = forms.ModelChoiceField(queryset=Consumer.objects.all(), label="Потребитель")
    gr = forms.ModelChoiceField(queryset=Grade.objects.all(), label="Марка стали")

    
class AddDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kd'].empty_label = "Вид продукции не выбран"
        self.fields['con'].empty_label = "Потребитель не выбран"
        self.fields['gr'].empty_label = "Марка стали не выбрана"
    
    class Meta:
        model = Chart
        fields = ['form', 'diameter', 'value1', 'value2', 'value3', 'time_measure', 'kd', 'con', 'gr']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }    
    
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        # fields = ('username', 'email', 'password1', 'password2')
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
        
        
        