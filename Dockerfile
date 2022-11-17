FROM python:3.8

ADD app.py templates

RUN pip install requests Flask render_template

CMD ["python", "./app.py" ]