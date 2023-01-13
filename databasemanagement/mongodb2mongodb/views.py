from django.shortcuts import render
from pymongo import MongoClient
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