#!/usr/bin/env python3
"""Using Redis with python"""
import redis
import uuid


class Cache:
    def __init__(self) -> None:
        """
        Create a Redis client instance and store it as a private variable
        """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data):
        """generate a random key and store the input data in Redis

        Args:
            data (any): can be a str, bytes, int or float.

        Returns:
            _type_: return the random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
