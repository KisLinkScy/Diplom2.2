from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='my_profile'),
    path('get_user_id/', views.get_user_id, name='get_user_id'),
]
