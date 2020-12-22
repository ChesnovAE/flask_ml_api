FROM python:3.8-alpine


COPY ./ /web/
WORKDIR /web/

RUN pip3 install -r requirements.txt

CMD [ "python3", "run.py" ]