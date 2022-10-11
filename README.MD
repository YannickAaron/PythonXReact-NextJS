# React (Nextjs/SSR) with Python FastAPi Backend POC

This is a POC project of a React (Nextjs/SSR) frontend with a Python FastAPi backend.
Goal is to learn how interaction of the two frameworks works and how to deploy them.

I want to use this repo to explore the possibilites of using machine learning in a web application.

## Application parts
1. Nextjs frontend: yarn dev
2. FastApi backend: uvicorn main:app --reload
3. Redis: docker run --name redis -p 6379:6379 -d redis
4. Celer: celery -A main worker -l info

## What do I use?
- nextjs
- fastapi
- uvicorn
- docker
- celery
- redis
- prisma

## Why Celery?
Celery is an open source, asynchronous task queue that is frequently used in conjunction with Python-based web frameworks such as FastAPI, Django, or Flask to manage background work outside of the typical request/response cycle. In other words, instead of forcing the user to wait for the task to finish, you can return an HTTP response immediately and run the process as a background task.

It's worth noting that you can leverage FastAPI's BackgroundTasks class, which comes directly from Starlette, to run tasks in the background.

So, why did i decide to use Celery be used instead of BackgroundTasks? 
1. Intensive tasks: Because BackgroundTasks runs in the same event loop as your app's requests, Celery should be used for tasks that perform heavy background computations like machine learning.
2. Frequently, you'll want to retrieve a job's status and then take some action based on it, such as sending an error email, starting a different background task, or retrying the task. Celery handles everything for you.

# Notes

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