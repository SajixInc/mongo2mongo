from django.shortcuts import render
from pymongo import MongoClient
from .localtoserver import localtostagging
from .servertoserver import staggingtoprod
from .servertolocal import dddd
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
        username1 = request.POST.get('Username')
        password1 = request.POST.get('Password')
        username2 = request.POST.get('UserName2')
        password2 = request.POST.get('password2')
        from_database = request.POST.get('from_database')
        ipaddress = request.POST.get('ipaddress')
        ipaddress1 = request.POST.get('ipaddress1')
        print(';;;;;;;;;;;;;;;;;;;;;',ipaddress1)
        staggingtoprod(from_database,username1,password1,username2,password2,to_database,ipaddress,ipaddress1)
    else:
        print('Fail')
    return render(request,'inndex4.html')





