#!/usr/bin/env python3

from os import chdir
from pathlib import Path
from subprocess import call
from urllib.request import urlopen


def download_ide(link: str) -> None:
    chdir(Path.home())
    call("wget " + link, shell=True)
    print("Unpacking...")
    call("tar -xf " + link.split("/")[-1], shell=True)
    print("Done\n")


def parser_feed(parser, req):
    with urlopen(req) as response:
        parser.feed(response.read().decode("utf-8"))


def get_ide_updates(ide_names: list, product_updates: dict) -> dict:
    ide_updates: dict = {}

    for name in ide_names:
        for key, value in product_updates.items():
            if isinstance(name, tuple) and name[0] == key:
                ide_updates[name] = value
            elif name == key:
                ide_updates[name] = value

    return ide_updates
