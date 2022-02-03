# Base image
FROM python:3.7

# Environment
ENV HOME /home
WORKDIR $HOME
COPY .bashrc requirements.txt $HOME/

# Installl commands
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
    less

# Install Python libraries
RUN pip install --upgrade pip \
    && pip install -r $HOME/requirements.txt \
    && pip install -i https://test.pypi.org/simple/ richcat