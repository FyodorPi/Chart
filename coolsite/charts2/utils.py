import matplotlib.pyplot as plt
import base64
from io import BytesIO
from matplotlib.ticker import *

from django.db.models import Count
from .models import *

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y):    
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Контрольная карта')
    y_second = y.copy()
    y_second.pop(0)
    y_first = y.copy()
    y_first.pop(-1)
    y_first = [n*(-1) for n in y_first]
    mr = [*map(sum, zip(y_second, y_first))]
    mr = [abs(n) for n in mr]
    x1 = list(range(0, len(x)))
    x2 = list(range(1, len(x)))
    
    ax1 = plt.subplot(211)
    plt.plot(x1, y, '-bo')
    plt.ylabel('Среднее значение Xср')
    ax1.set(xlim=(-0.2, len(x)-1+0.2))
    ax1.xaxis.set_major_formatter(NullFormatter())

    ax2 = plt.subplot(212)
    plt.plot(x2, mr, '-bo')
    plt.xticks(rotation=90)
    # plt.xlabel('Дата')
    plt.ylabel('Скользящий размах MR')
    ax2.set(xlim=(-0.2, len(x)-1+0.2))
    ax2.xaxis.set_major_locator(FixedLocator(range(0, len(x))))
    # ax2.xaxis.set_major_formatter(FixedFormatter(x))
    ax2.xaxis.set_major_formatter(NullFormatter())
    plt.tight_layout()
    graph = get_graph()
    return graph
    
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Ввод данных", 'url_name': 'add_data'},
        # {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Построение карты", 'url_name': 'home'},        
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        # cons = Consumer.objects.annotate(Count('chart'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        return context
        
        # context['cons'] = cons
        # if 'cat_selected' not in context:
        #     context['cat_selected'] = 0
        
    # def get_user_context(self, **kwargs):
    #     context = kwargs
    #     cons = Consumer.objects.all()
    #     context['menu'] = menu
    #     context['cons'] = cons
    #     # if 'con_selected' not in context:
    #     #     context['con_selected'] = 0
    #     return context  