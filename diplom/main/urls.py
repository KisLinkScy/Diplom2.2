from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.loging, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registr/', views.registr_user, name='registr'),
    path('save/', views.save_data, name='save_data'),
    path('gaz/', views.gaz, name='gaz'),
    path('svet/', views.svet, name='svet'),
    path('voda/', views.voda, name='voda'),
]
