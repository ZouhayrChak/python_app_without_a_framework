from urls import urlpatterns
from app.views import users

def wsgi_application(environ,start_response):
    for urlpattern in urlpatterns:
        if urlpattern[0]==environ['PATH_INFO']:
                view=urlpattern[1]
                status_code='200 OK'
                response=view(environ)
    print(users)
    headers=[('CONTENT_LENGTH',str(len(response)))]
    
    start_response(status_code,headers)
    return [response]
