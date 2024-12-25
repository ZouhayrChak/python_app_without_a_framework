from urls import urlpatterns

def wsgi_application(environ,start_response):
    path=environ["PATH_INFO"]
    handler=urlpatterns.get(path,not_found_handler)
    print(handler)
    status_code='200 OK'
    response=handler(environ)
    headers=[("Content-Length",str(len(response)))]
    
    start_response(status_code,headers)
    return [response]

def not_found_handler(environ):
    return "404 Not Found".encode()

