FROM ubuntu

RUN apt update && apt install python3 -y &&  apt install python3-bs4 -y

WORKDIR /python_app

COPY . .

EXPOSE 8000

CMD ["python3" ,"./server.py"]   