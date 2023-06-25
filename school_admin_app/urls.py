from django.urls import path
from school_admin_app import views

urlpatterns=[
    path('login/', views.login,name='login'),
    path('admin_home/', views.admin_home,name='admin_home'),
    path('admin_home/add_school', views.add_school,name='add_school'),
]