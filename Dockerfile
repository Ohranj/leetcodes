FROM python:3-slim

ARG user=alex
ARG work_dir=/var/leet

WORKDIR $work_dir

COPY . .

RUN apt update
RUN apt upgrade -y
RUN apt install -y sudo curl

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -ms /bin/bash $user
RUN usermod -a -G root $user

#Shell in to container with user
USER $user