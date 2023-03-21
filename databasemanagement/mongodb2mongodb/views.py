from django.shortcuts import render
from pymongo import MongoClient
from .mian1 import localtostagging
from .main2 import staggingtoprod
from .mian import dddd
#
# if __name__ == '__main__':
#     import databasemanagement.main
import pymongo

import urllib.parse




def mongo(request):
    if request.method == 'POST':
        from_database = request.POST.get('from_database')
        print(from_database)
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        to_database = request.POST.get('to_database')
        to_host = request.POST.get('to_host')
        ipaddress = request.POST.get('ipaddress')
        dddd(from_database, Username, Password, to_database, to_host, ipaddress)
    else:
        print('Fail')
    return render(request,'inndex2.html')





def mongo2(request):
    if request.method == 'POST':
        to_database = request.POST.get('to_database')
        print(to_database)
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        from_database = request.POST.get('from_database')
        to_host = request.POST.get('to_host')
        ipaddress = request.POST.get('ipaddress')
        localtostagging(from_database, Username, Password, to_database, to_host, ipaddress)
    else:
        print('Fail')
    return render(request,'inndex3.html')


def mongo3(request):
    if request.method == 'POST':
        to_database = request.POST.get('to_database')
        print(to_database)
        Username = request.POST.get('Username')
        password = request.POST.get('Password')
        UserName = request.POST.get('Username')
        Password = request.POST.get('Password')
        from_database = request.POST.get('from_database')
        ipaddress = request.POST.get('ipaddress')
        ipaddress1 = request.POST.get('ipaddress1')
        staggingtoprod(from_database,Username,Password,to_database,ipaddress)
    else:
        print('Fail')
    return render(request,'inndex4.html')