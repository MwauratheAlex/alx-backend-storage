#!/usr/bin/env python3
"""Get page module"""
from typing import Callable
import requests
import redis
from functools import wraps


def cache_results(method: Callable) -> Callable:
    """cache results of method"""
    redis_instance = redis.Redis()

    @wraps(method)
    def wrapper(url):
        result_key = f'result:{url}'
        result = redis_instance.get(result_key)
        if result:
            return result.decode('utf-8')
        count_key = f'count:{url}'
        result = method(url)

        redis_instance.incr(count_key)
        redis_instance.set(result_key, result)
        redis_instance.expire(result_key, 10)
        return result
    return wrapper


@cache_results
def get_page(url: str) -> str:
    """uses the requests module to obtain the HTML content
    of a particular URL and returns it"""
    return requests.get(url).text
