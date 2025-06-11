#!/usr/bin/env python3
"""
File for advanced task 5. Implementing an expiring web cache and tracker
Uses the requests module to obain HTML content of a page and returns it.
"""

import requests
import redis

db = redis.Redis()


def get_page(url: str) -> str:
    """
    Gets the HTML content of a page from its URL
    :param url: URL of the page to pull HTML content from
    :return: The HTML content of the given page
    """
    db.incr(f"count:{url}")

    html = db.get(url)
    if html is None:
        html = requests.get(url).text
        db.set(url, html, ex=10)
    else:
        html = html.decode("UTF-8")

    return html
