#!/usr/bin/env python3
"""Get page module"""
from typing import Callable
import requests
import redis
from functools import wraps

redis_instance = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """counts how many times a url was called"""

    @wraps(method)
    def wrapper(url):
        key = f'count:{url}'
        redis_instance.incr(key)
        return method(url)
    return wrapper


def cache_results(method: Callable) -> Callable:
    """cache results of method"""

    @wraps(method)
    def wrapper(url):
        key = f'cache:{url}'
        result = redis_instance.get(key)
        if result is not None:
            return result.decode('utf8')
        result = method(url)
        redis_instance.setex(key, 10, result)
        redis_instance.set(f'count:{url}', 0)
        return result
    return wrapper


@count_calls
@cache_results
def get_page(url: str) -> str:
    """uses the requests module to obtain the HTML content
    of a particular URL and returns it"""
    return requests.get(url).text
