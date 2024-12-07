
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexc, name='indexc'),
    path('run_code/', views.run_code, name='run_code'),
]
