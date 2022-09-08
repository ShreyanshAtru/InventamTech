# from django.conf.urls import url
from django.urls import path, include
from .views import LoginAPIView, RegisterApi
from .import views


urlpatterns = [
    path('customer/register', RegisterApi.as_view()),
    path('home_page/<str:id>/', views.home_page, name='home'),
    path('signup', views.signup, name='signup'),
    path('resturant', views.resturant, name='resturant'),
    path('customer/login', LoginAPIView.as_view()),
]
