from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.first,name='first'),
    path('first_page',views.first_page,name='first_page'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('',views.first,name='first'),
    path('contact_us_in',views.contact_us_in,name='contact_us_in'),
    path('contact_us_out',views.contact_us_out,name='contact_us_out'),
    path('ancmnt',views.ancmnt,name='ancmnt'),
    path('ancmnt_view',views.ancmnt_view,name='ancmnt_view'),
    path('logout',views.logout,name='logout'),
    path('change_psw',views.change_psw,name='change_psw'),
    path('direct',views.Inbox,name='Inbox'),
    path('directs', views.Directs, name='directs'),
     path('send_direct', views.SendDirect, name='send_direct'),
     path('my_profile_view',views.my_profile_view,name='my_profile_view'),
     path('profile_view',views.profile_view,name='profile_view'),
     path('contacts',views.contacts,name='contacts'),
     path('like_unlike_post',views.like_unlike_post,name='like_unlike_post'),

    ]