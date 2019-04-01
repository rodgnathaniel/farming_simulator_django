from django.urls import path

from . import views



app_name = 'farm'

urlpatterns = [    
    path('', views.home_view, name='home'),
    path('save_state/', views.save_state, name='save_state'),
]