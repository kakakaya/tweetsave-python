#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kakakaya, Date: Sat Feb  4 22:57:03 2017
# from pprint import pprint as p
"""Core module of tweetsave library.
This could be import and use for other product.
"""

import requests

TWEETSAVE_URL = "https://tweetsave.com/api.php"


def save(target: str) -> dict:
    """Save tweet at TweetSave, and print out it's url if succeed.

    Args:
    target -- Status URL or Status ID

    Yields:
    response from tweetsave.com
    """
    response = requests.get(TWEETSAVE_URL, params={
        "mode": "save",
        "tweet": target
    })
    if response.ok:
        result = response.json()
    else:
        result = {"errors": [response.reason]}
    return result


def stream(target_id: str) -> list:
    items = []
    page = 1
    while True:
        resp = requests.get(TWEETSAVE_URL, params={
            "mode": "stream",
            "stream": "saves",
            "page": page,
            "target_id": target_id
        })
        if resp.ok:
            data = resp.json()
            if type(data) is dict:
                if "No more results" in data["errors"]:
                    break       # このときだけ抜ける
                else:
                    return data["errors"]
            else:
                items += data
                page += 1       # 次のページを参照する
        else:
            continue
    return items


if __name__ == "__main__":
    print("Don't call api directory; use cli.py instead (or tweetsave command).")
