# Base image
FROM python:3.7

# Environment
ENV HOME /home
WORKDIR $HOME
COPY requirements.txt $HOME/

# Installl commands
RUN apt-get update && apt-get upgrade -y

# Install Python libraries
RUN pip install --upgrade pip \
    && pip install -r $HOME/requirements.txt