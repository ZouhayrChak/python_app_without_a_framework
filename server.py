from wsgiref import simple_server
from wsgi import wsgi_application





with simple_server.make_server('',8000,app=wsgi_application) as s:
    print(""" connecting to the server
        http://localhost:8000
       
     
    """)
    s.serve_forever()




