https://fastapi.tiangolo.com/advanced/websockets/

https://medium.com/cuddle-ai/async-architecture-with-fastapi-celery-and-rabbitmq-c7d029030377

poetry run uvicorn main:app --reload

https://towardsdatascience.com/deploying-ml-models-in-production-with-fastapi-and-celery-7063e539a5db


start celery worker
```
poetry run celery -A main.celery worker --loglevel=info -Q universities,university
```

https://github.com/GregaVrbancic/fastapi-celery/blob/master/app/worker/celery_app.py

https://www.youtube.com/watch?v=puy3LdG2nYA