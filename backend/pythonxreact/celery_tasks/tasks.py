from typing import List

from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
    name="universities:get_all_universities_task",
)
def get_all_universities_task(self, countries: List[str]):
    data: dict = {}
    data = {"countries": countries}
    return data


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
    name="university:get_university_task",
)
def get_university_task(self, country: str):
    data = {"country": country}
    return data


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
    name="university:get_university_task",
)
def get_university_task(self, country: str):
    data = {"country": country}
    return data


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
    name="test:count_to_X",
)
def get_university_task(self, X: int):
    data = {"country": country}
    return data
