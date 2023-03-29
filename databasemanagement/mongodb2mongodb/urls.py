from django.urls import path,include

from .views import mongo,mongo2,mongo3

urlpatterns = [
    path('servertolocal',mongo),
    path('localtoserver',mongo2),
    path('servertoserver',mongo3),

]