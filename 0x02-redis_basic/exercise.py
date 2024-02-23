import redis
import uuid
"""Redis Cache module"""


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: (str | bytes | int | float)) -> str:
        """Stores data into redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
