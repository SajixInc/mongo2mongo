from django.urls import path,include

from .views import mongo,mongo2

urlpatterns = [
    path('staggingtolocal',mongo),
    path('localtostagging',mongo2),

]