FROM python:3.9-slim

COPY ./pythonxreact /backend
COPY ./pyproject.toml main.py /backend/
WORKDIR /backend

RUN pip install --upgrade pip
RUN pip3  install -e .

#ENTRYPOINT ["python3"]
#CMD ["main.py"]