#!/usr/bin/env python3
"""Get page module"""
from typing import Callable
import requests
import redis
from functools import wraps

redis_instance = redis.Redis()


def cache_results(method: Callable) -> Callable:
    """cache results of method"""

    @wraps(method)
    def wrapper(url):
        redis_instance.incr(f'count:{url}')
        result = redis_instance.get(f'result:{url}')
        if result:
            return result.decode('utf8')
        result = method(url)
        redis_instance.set(f'count:{url}', 0)
        redis_instance.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@cache_results
def get_page(url: str) -> str:
    """uses the requests module to obtain the HTML content
    of a particular URL and returns it"""
    return requests.get(url).text
