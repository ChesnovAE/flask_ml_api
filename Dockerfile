FROM python:3.8-slim

WORKDIR /ml_api/
ADD ./requirements.txt /ml_api/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./ /ml_api/
WORKDIR /ml_api/

CMD [ "sh", "gunicorn_run.sh" ]