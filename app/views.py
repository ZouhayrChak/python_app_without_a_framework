from bs4 import BeautifulSoup
import urllib
import sqlite3
users=[]
def index(request):
    soup=BeautifulSoup(open('app/templates/index.html'),'html.parser').encode('utf-8')
    if request['REQUEST_METHOD']=='POST':
        input_obj=request["wsgi.input"]
        input_length=int(request["CONTENT_LENGTH"])
        body=input_obj.read(input_length).decode()
        data_r=urllib.parse.parse_qs(body,keep_blank_values=True) 
        if data_r not in users: 
            users.append(data_r)
        print(users)
    
    return soup


def new(request):
    return b"That's new!!!!!!"


def other(request):
    return b'other'