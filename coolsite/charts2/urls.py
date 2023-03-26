from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    # path('', ChartListView.as_view(), name='home'),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('adddata/', AddData.as_view(), name='add_data'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
