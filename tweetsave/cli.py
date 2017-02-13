#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kakakaya, Date: Sat Feb  4 18:59:53 2017
# from pprint import pprint as p
"""Cli tool for tweetsave.com.
"""

import click
from tweetsave import api
from sys import exit


@click.group()
def cli():
    pass


@cli.command()
@click.argument("target_id", type=str)
def list(target_id: str):
    """Show current list on TweetSave.

    Args:
    target_id -- TweetSave ID for Save list.
                 For example, if you want to get data from https://tweetsave.com/saves/XjEtT, use XjEtT.
    """
    result = api.stream(target_id)
    if len(result) == 0:
        # 何も得られない
        print("Nothing saved yet.")
    elif type(result[0]) is str:
        # エラーを表示する
        print("\n".join(result))
    else:
        for item in result:
            print("@{item[user][screen_name]}: {item[text]}".format(item=item))


@cli.command()
@click.argument("target", type=str)
def save(target: str):
    """Save tweet at TweetSave, and print out it's url if succeed.

    Args:
    target -- Status URL or Status ID
    """
    result = api.save(target)
    status = result.get("status")
    if status and status == "OK":
        print(result.get("redirect"))
    else:
        exit("\n".join(result.get("errors")))


def main():
    cli()


if __name__ == "__main__":
    main()
