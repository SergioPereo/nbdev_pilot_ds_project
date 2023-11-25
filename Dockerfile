# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /nbdev

RUN apt-get update

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


COPY . /nbdev

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser



# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD jupyter trust nbs/00_bloom_filter.ipynb && jupyter trust nbs/01_trie.ipynb && jupyter notebook --ip='*' --NotebookApp.token='' --NotebookApp.password='' --allow-root