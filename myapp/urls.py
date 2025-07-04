

from django.urls import path
from . import views


urlpatterns = [
    path('',views.home ,name = 'home'),
    path('about/', views.about , name = 'about'),
    path('index/', views.index , name = 'index'),
    path('form/', views.form , name = 'form'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
