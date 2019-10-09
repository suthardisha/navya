
from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.IndexView,name="register"),
    path('registration/',views.registeruser,name="registration"),
    
]