from django.urls import path,include

from .views import mongo

urlpatterns = [
    path('',mongo)

]