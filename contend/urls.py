from django.urls import path
from . import views

urlpatterns = [
    path('contend',views.contend,name='contend'),
]