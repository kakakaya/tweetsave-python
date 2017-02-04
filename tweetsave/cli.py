#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kakakaya, Date: Sat Feb  4 18:59:53 2017
# from pprint import pprint as p
"""Cli tool for tweetsave.com.
"""

import click
from . import api


@click.group()
def cli():
    pass


@cli.command()
def list():
    """Show current list on TweetSave.
    """
    raise NotImplementedError("No public API published.")


@cli.command()
@click.argument("target", type=str)
def save(target: str):
    """Save tweet at TweetSave, and print out it's url if succeed.

    Args:
    target -- Status URL or Status ID
    """
    result = api.ave(target)
    status = result.get("status")
    if status and status == "OK":
        print(result.get("redirect"))
    else:
        "\n".format(result.get("errors"))


def main():
    cli()


if __name__ == "__main__":
    main()
