from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
urlpatterns = [
    # path('',views.home,name="home"),
    path('signup', views.signup,name='signup'),
    path('signout', views.signout,name="signout"),
    path('signin', views.signin,name='signin'),
    path('topper_images/',views.topper_images,name="topper_images"),
    path('image_list/', views.image_list,name='image_list'),
    path('farmacy/', views.farmacy,name='farmacy'),
    path('about/', views.about,name='about'),
    path('display_first_three_images/', views.display_first_three_images,name='display_first_three_images'),
    path('ibt/',views.ibt,name="ibt"),
    path('news/',views.news,name="news"),
    path('shetivpashupalan/',views.shetivpashupalan,name="shetivpashupalan"),
    path('urjavparyavaran/',views.urjavparyavaran,name="urjavparyavaran"),
    path('gruhvarogya/',views.gruhvarogya,name="gruhvarogya"),
    path('abhiyantriki/',views.abhiyantriki,name="abhiyantriki"),
    path('newsdetails/<newsid>',views.newsDetails,name="newsdetails"),
    path('', views.window,name='window')
    
]