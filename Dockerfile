FROM python:3.9-slim-buster


WORKDIR / my-model

COPY GotchaAPP ./GotchaAPP
COPY key.json ./key.json
COPY model.sav ./model.sav
COPY requirement.txt ./requirement.txt

RUN apt-get update && \
    apt-get -y install sudo && \ 
    sudo apt-get upgrade

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirement.txt
COPY run.py ./run.py


EXPOSE 5000
ENV GOOGLE_APPLICATION_CREDENTIALS=./key.json

CMD ["python3", "run.py"]
