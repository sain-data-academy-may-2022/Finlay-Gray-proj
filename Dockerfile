FROM python:3.10.4

WORKDIR /usr/src

COPY src/ .

RUN pip3 install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python3", "app.py"]