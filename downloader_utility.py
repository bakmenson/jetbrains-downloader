#!/usr/bin/env python3

from os import chdir
from pathlib import Path
from subprocess import run
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from sys import exit


def download_ide(link: str) -> None:
    chdir(Path.home())
    run("wget " + link, shell=True, check=True)


def parser_feed(parser, req):
    try:
        with urlopen(req, timeout=10) as response:
            parser.feed(response.read().decode("utf-8"))

        if not parser.get_product_updates():
            print("\nData not retrieved because <wrong url>.\n")
            exit()

    except (HTTPError, URLError) as error:
        print(f"\nData not retrieved because {error}.\n")
        exit()


def get_ide_updates(ide_names: list, product_updates: dict) -> dict:
    ide_updates: dict = {}

    for name in ide_names:
        for key, value in product_updates.items():
            if isinstance(name, tuple) and name[0] == key:
                ide_updates[name] = value
            elif name == key:
                ide_updates[name] = value

    return ide_updates


def extract_tar_archive(path_to_file: str) -> None:
    print("Unpacking...")
    run("tar -xf " + path_to_file, shell=True, check=True)
