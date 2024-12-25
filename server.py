from waitress import serve


from wsgi import wsgi_application


if __name__=="__main__":
        serve(wsgi_application, port='8000')


