FROM python:2.7

MAINTAINER  Youssef Hbali "youssef.hbali@gmail.com"


COPY . /webapp

WORKDIR /webapp/

RUN pip install -r requirements.txt


WORKDIR /webapp/app

ENTRYPOINT [ "python" ]

CMD [ "app-ml.py" ]
