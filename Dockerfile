FROM python:3.9.1

WORKDIR /app/
COPY ./requirements.txt .
COPY ./srcs/app.py app.py

RUN pip install --upgrade pip \
&& pip install -r requirements.txt \
&& groupadd -r test && useradd -r -g test testuser

USER testuser
CMD [ "python","app.py","1" ,"2"]
