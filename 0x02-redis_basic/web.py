#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import requests
import redis
from functools import wraps

r = redis.Redis()


def cache_page(func):
    """_summary_

    Args:
        func (_type_): callable
    """
    @wraps(func)
    def wrapper(url):
        """
        track how many times a particular URL was accessed,
        in the key "count:{url}" and cache the result,
        with an expiration time of 10 seconds.
        """
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"

        # Check if the page is already cached
        cached_page = r.get(cache_key)
        if cached_page:
            print("Returning cached page")
            return cached_page.decode('utf-8')

        # If not cached, get the page content
        page_content = func(url)

        # Cache the page content with a 10-second expiration
        r.setex(cache_key, 10, page_content)

        # Increment the access count for the URL
        r.incr(count_key)

        return page_content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """It uses the requests module to obtain the,
    HTML content of a particular URL 

    Args:
        url (str):

    Returns:
        str: text content or html content
    """
    response = requests.get(url)

    return response.text
