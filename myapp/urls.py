

from django.urls import path
from . import views


urlpatterns = [
    path('',views.home ,name = 'home'),
    path('about/', views.about , name = 'about'),
    path('index/', views.index , name = 'index'),
    path('form/', views.form , name = 'form'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('add-student/', views.create_student, name='add_student'),
    path('success/', views.success, name='success'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),

]
