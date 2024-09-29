from utils import path
from app.views import index,new,other 


urlpatterns=[
    ('/',index),
    ('/New',new),
    ('/New/Else',other)
]


