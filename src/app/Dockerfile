FROM python:3.8-slim

WORKDIR /app

RUN useradd -ms /bin/bash taxapp && \
  apt-get update && apt-get install curl unixodbc-dev gnupg2 --yes && \
  apt-get update

COPY --chown=taxapp . .
RUN mkdir /home/taxapp/.postgresql
COPY ./root.crt /home/taxapp/.postgresql/root.crt
RUN pip install -r /app/requirements.txt


USER taxapp
CMD [ "python3", "manage.py", "run" ]
