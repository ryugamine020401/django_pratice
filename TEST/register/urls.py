from . import views
from django.urls import path

urlpatterns =[
    path('', views.register , name='Logout'),
    path('register', views.sign_up, name='Register'),
    path('login', views.sign_in, name='Login'),
    path('logout', views.log_out, name='Logout')
]