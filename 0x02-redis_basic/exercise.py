#!/usr/bin/env python3
from collections.abc import Callable
import redis
import uuid
from typing import Optional, Union
"""Redis Cache module"""


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data into redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]):
        """Gets data for key from redis"""
        value = self._redis.get(key)
        if value == "nil":
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str):
        """Gets data for key from redis as string"""
        return self.get(key, str)

    def get_int(self, key: str):
        """Gets data for key from redis as an int"""
        return self.get(key, int)
