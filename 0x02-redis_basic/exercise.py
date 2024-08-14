#!/usr/bin/env python3
"""Using Redis with python"""
import redis
import uuid
from typing import Callable, Optional, Union


class Cache:
    def __init__(self) -> None:
        """
        Create a Redis client instance and store it as a private variable
        """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data) -> str:
        """generate a random key and store the input data in Redis

        Args:
            data (any): can be a str, bytes, int or float.

        Returns:
            str: return the random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        convert the data back to the desired format.

        Args:
            key (str):
            fn (Optional[Callable], optional): If a callable is provided,
            use it to convert the data. Defaults to None.

        Returns:
            _type_: recovering original type
        """
        result = self._redis.get(key)
        if result is not None and fn is not None:
            result = fn(result)

        return result

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the data as a UTF-8 decoded string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the data as an integer
        """
        return self.get(key, fn=int)
