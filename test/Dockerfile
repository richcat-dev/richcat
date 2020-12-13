# Base image
FROM python:3.7

# Environment
ENV HOME /home
WORKDIR $HOME
COPY .bashrc requirements.txt $HOME/

# Install Commands
RUN apt-get update && apt-get upgrade -y \
  && apt-get install -y \
    git \
    vim

# Install Python libraries
RUN pip install --upgrade pip \
  && pip install -r $HOME/requirements.txt

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
  && apt-get install -y nodejs \
  && npm install n -g \
  && n stable \
  && apt-get purge -y nodejs npm

# Install Jupyter Lab Extensions
RUN pip install ipywidgets \
  && jupyter nbextension enable --py --sys-prefix widgetsnbextension \
  && jupyter labextension install \
    @jupyter-widgets/jupyterlab-manager \
    @lckr/jupyterlab_variableinspector \
    @jupyterlab/toc

