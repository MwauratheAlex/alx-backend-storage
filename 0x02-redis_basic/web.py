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
        result_key = f'result:{url}'
        count_key = f'count:{url}'
        redis_instance.incr(count_key)
        result = redis_instance.get(result_key)
        if result is not None:
            return result.decode('utf8')
        result = method(url)
        redis_instance.setex(result_key, 10, result)
        return result
    return wrapper


@cache_results
def get_page(url: str) -> str:
    """uses the requests module to obtain the HTML content
    of a particular URL and returns it"""
    return requests.get(url).text
