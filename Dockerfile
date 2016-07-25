FROM ubuntu:14.04

COPY app.py /

EXPOSE 8080

CMD /usr/bin/python3 /app.py