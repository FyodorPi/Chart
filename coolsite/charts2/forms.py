from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ChartsSearchForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices_kd = Kind.objects.order_by('name')
        choices_con = Consumer.objects.order_by('name')
        choices_con = Grade.objects.order_by('name')
        choice_list_kd = []
        choice_list_con = []
        choice_list_gr = []

        for item in choices_kd:
            choice_list_kd.append(item)
        self.fields['kd'].choices = choice_list_kd
        for item in choices_kd:
            choice_list_con.append(item)
        self.fields['con'].choices = choice_list_con
        for item in choices_kd:
            choice_list_gr.append(item)
        self.fields['gr'].choices = choice_list_gr

    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Начальная дата")
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Конечная дата")
    # kd = forms.ChoiceField(choices=[(n.id, n.name) for n in Kind.objects.order_by('name')], label="Вид продукции")
    kd = forms.ChoiceField(label="Вид продукции")
    # con = forms.ChoiceField(choices=[(m.id, m.name) for m in Consumer.objects.order_by('name')], label="Потребитель")
    con = forms.ChoiceField(label="Потребитель")
    # gr = forms.ChoiceField(choices=[(x.id, x.name) for x in Grade.objects.order_by('name')], label="Марка стали")
    gr = forms.ChoiceField(label="Марка стали")

    
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
    
        
        
        