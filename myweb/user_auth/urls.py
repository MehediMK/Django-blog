from django.urls import path

from . import views
urlpatterns = [
    path('login/',views.ulogin,name='login'),
    path('logout/',views.ulogout,name='logout'),
    path('register/',views.usrr_regi,name='register'),
    path('editinfo/',views.editinfo,name='editinfo'),
    path('profile/',views.profile,name='profile'),
    path('change/password/',views.change_password,name='cngpass'),
]