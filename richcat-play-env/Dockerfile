# Base image
FROM python:3.7

# Environment
ENV HOME /home
WORKDIR $HOME
COPY .bashrc $HOME/

# Installl commands
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
    less

# Install Python libraries
RUN pip install --upgrade pip