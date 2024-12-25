from bs4 import BeautifulSoup
import urllib
import sqlite3




def index(request):
    soup=BeautifulSoup(open('templates/index.html'),'html.parser').encode('utf-8')
    if request['REQUEST_METHOD']=='POST':
        input_obj=request["wsgi.input"]
        input_length=int(request["CONTENT_LENGTH"])
        body=input_obj.read(input_length).decode()
        data_r=urllib.parse.parse_qs(body,keep_blank_values=True) 
        cx = sqlite3.connect("test.db")
        cu = cx.cursor()
        if (data_r["first name"][0], data_r["last name"][0], data_r["email"][0], data_r["password"][0]) not in cu.execute("select * from users").fetchall():
            cu.execute("insert into users values (?, ?, ?, ?)", (data_r["first name"][0], data_r["last name"][0], data_r["email"][0], data_r["password"][0]))
            cx.commit()
            
        print(cu.execute("select * from users").fetchall())
        cx.close()
    
    return soup
    

def new(request):
    
    return b"That's new!!!!!!"


def other(request):
    return b'other'




