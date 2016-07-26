FROM ubuntu:14.04

# Install pip.
COPY get-pip.py /
RUN /usr/bin/python3 /get-pip.py

RUN mkdir /app
ADD * /app/
RUN pip install -r /app/requirements.txt

RUN /usr/bin/python3 /app/initdb.py

EXPOSE 8080

CMD /usr/bin/python3 /app/app.py