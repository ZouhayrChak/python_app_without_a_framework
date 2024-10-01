Have you ever asked yourself, how to create a python application without using a framework like django, bottle or Flask ?
This is the answer: No!
Because actually they give us everything we need to create an application easily and in a time record.
Here I am diving deep to what's hidden behind the functionning of those frameworks.

What does the HTTP has to do with Python ? How to tell Python we want this view to appear when going to a certain URL ?
Actually, Python has a bench of libraries that allow us to communicate with a server; It creates its own server. Some of them are the "requests" library.
But what I am using here is the "Wsgiref" library which is a reference implementation of the WSGI protocol; 
When sending a request to our server in a given port, it reacts by invoking the WSGI_Application which is standardized based on the CGI standards. It takes two aguments:
  -- the "Environ" dictionary which is a result of parsing the HTTP request, it contains environment variables. 
  -- "start_response" function takes two arguments, the "Status_code" of the Response ,and the "Headers".

The application return an iterable"[response]" and response must be in bytes.


