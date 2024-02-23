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
        redis_instance.incr(f'count:{url}')
        result = redis_instance.get(f'result:{url}')
        if result is not None:
            return result.decode('utf8')
        result = method(url)
        redis_instance.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@cache_results
def get_page(url: str) -> str:
    """uses the requests module to obtain the HTML content
    of a particular URL and returns it"""
    return requests.get(url).text
