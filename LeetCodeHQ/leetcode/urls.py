
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.code_list, name='code_list'),
    path('code/<int:cid>/', views.code_detail, name='code_detail'),
]