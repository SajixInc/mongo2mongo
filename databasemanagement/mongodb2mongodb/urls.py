from django.urls import path,include

from .views import mongo,mongo2,mongo3

urlpatterns = [
    path('staggingtolocal',mongo),
    path('localtostagging',mongo2),
    path('staggingtoprod',mongo3),

]