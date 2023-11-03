from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('shop/', views.shop, name = "shop"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('faq/', views.faq, name = "faq"),
]