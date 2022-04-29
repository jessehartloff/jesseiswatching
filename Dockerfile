FROM python:3.8

ENV HOME /root
WORKDIR /root

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "watching_app.py"]
