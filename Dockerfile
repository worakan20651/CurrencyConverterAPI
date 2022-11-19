FROM python:3.7

WORKDIR /src/app.py

RUN apt-get update 
RUN pip install flask
RUN pip install requests

COPY . .

CMD [ "python", "app.py" , "8080"]