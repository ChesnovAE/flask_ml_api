FROM python:3.8-alpine


COPY ./ /ml_api/
WORKDIR /ml_api/

RUN pip3 install -r requirements.txt

CMD [ "python3", "run.py" ]