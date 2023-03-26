from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from statistics import mean
# from math import isnan
# from itertools import filterfalse
# from django_tables2 import SingleTableView
# import numpy as np

# from .tables import *
from .utils import *
from .models import *
from .forms import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Ввод данных", 'url_name': 'add_data'},
        # {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Построение карты", 'url_name': 'home'},
]

def index(request):
    objs = None
    chart1 = None
    n = 0
    # table = None
    search_form = ChartsSearchForm(request.POST or None)
    
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        kd = request.POST.get('kd')
        con = request.POST.get('con')
        gr = request.POST.get('gr')
        objs = Chart.objects.filter(time_measure__lte=date_to, time_measure__gte=date_from, kd=kd, con=con, gr=gr).order_by('time_measure', 'time_create')


        if len(objs) > 0:
            x = [x.time_measure for x in objs]
            y = [[y.value1, y.value2, y.value3] for y in objs]
            y = [[n for n in m if n] for m in y]
            y = [mean(m) for m in y]
            chart1 = get_plot(x, y) 
        else:
            messages.warning(request, "Apparently no data available...")    
        
        n = range(1, len(objs)+1)
        # coll = {'Номер': [x for x in range(1, len(objs))]
        #         'Дата': [x.time_measure for x in objs], 
        #         'Форма': [x.form for x in objs]
        # }
        # table = NameTable(coll)
        
    context = {
        'objs': objs,
        'n': n,
        'chart1': chart1,
        'menu': menu,        
        'title': '',
        'search_form': search_form,
        # 'table': table,
    }    
    
    return render(request, 'charts2/index.html', context=context)

def about(request):
    return render(request, 'charts2/about.html', {'menu': menu, 'title': 'О сайте'})

class AddData(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddDataForm
    template_name = 'charts2/adddata.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ввод данных")
        context = dict(list(context.items()) + list(c_def.items()))
        return context
        
 

# class AddData(CreateView):
#     form_class = AddDataForm
#     template_name = 'charts2/adddata.html'
#     success_url = reverse_lazy('home')

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Ввод данных'
#         context['menu'] = menu
#         return context

# def adddata(request):
#     if request.method == 'POST':
#         form = AddDataForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = AddDataForm()
#     return render(request, 'charts2/adddata.html', {'form': form, 'menu': menu, 'title': 'Ввод данных'})

def contact(request):
    return HttpResponse("Обратная связь")
 
def login(request):
    return HttpResponse("Авторизация")


def consumers(request, conid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Потребители</h1><p>{conid}</p>")

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'charts2/register.html'
    success_url = reverse_lazy('login')
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'charts2/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

