
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexc, name='indexc'),
    path('coding/', views.coding, name='coding'),
]
