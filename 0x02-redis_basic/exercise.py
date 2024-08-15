#!/usr/bin/env python3
"""Using Redis with python"""
import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def replay(method: Callable) -> None:
    """display the history of calls of a particular function

    Args:
        method (_type_): callable
    """
    if method is None or not hasattr(method, '__self__'):
        return

    _redis = getattr(method.__self__, '_redis', None)

    if not isinstance(_redis, redis.Redis):
        return
    key = method.__qualname__

    count = int(_redis.get(key))
    print("{} was called {} times:".format(key, count))

    list_inputs = _redis.lrange(f"{key}:inputs", 0, -1)
    list_outputs = _redis.lrange(f"{key}:outputs", 0, -1)

    for inputs, outputs in zip(list_inputs, list_outputs):
        print('{}(*{}) -> {}'.format(
            key,
            inputs.decode("utf-8"),
            outputs.decode("utf-8")
        ))


def call_history(method: Callable) -> Callable:
    """"Define the call_history decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """store the history of inputs and outputs for a particular function"""
        key = method.__qualname__

        input_key = f'{key}:inputs'
        output_key = f'{key}:outputs'

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """Define the count_calls decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increments the count for key every time the method is called,

        Returns:
            _type_: returns the value returned by the original method.
        """
        key = method.__qualname__

        self._redis.incr(key)

        # Call the original method and return its value
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self) -> None:
        """
        Create a Redis client instance and store it as a private variable
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
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
