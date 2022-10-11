FROM python:3.9-slim

#copy pythonxreact pyproject.toml and main.py and nothing else
COPY . /backend

WORKDIR /backend

RUN pip install --upgrade pip
RUN pip3 install -e .

#ENTRYPOINT ["python3"]
#CMD ["main.py"]