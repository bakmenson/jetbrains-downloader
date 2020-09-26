#!/usr/bin/env python3

from os import chdir
from sys import exit
from pathlib import Path
from subprocess import call
from urllib.request import urlopen, Request

from jetbrains_updates_parser import JetbrainsUpdatesParser
from choose_ide import ChooseIde


def download_jetbrains_ide(link: str, ide_name: str) -> None:
    call("wget " + link + ide_name, shell=True)
    print("Unpacking...")
    call("tar zxf " + ide_name, shell=True)
    print("Done\n")


ide_array: tuple = ("IDEA", "Pycharm")

ide_number = ChooseIde.choose_ide(ide_array)

if ide_number == len(ide_array) + 1:
    exit()

req = Request("https://www.jetbrains.com/updates/updates.xml")
html_parser = JetbrainsUpdatesParser()

with urlopen(req) as response:
    html_parser.feed(response.read().decode("utf-8"))

products = html_parser.get_result_data()

idea_community: str = f'ideaIC-{products["IC-IU-RELEASE-licensing-RELEASE"]}.tar.gz'
idea_ultimate: str = f'ideaIU-{products["IC-IU-RELEASE-licensing-RELEASE"]}.tar.gz'

pycharm_community: str = f'pycharm-community-{products["PC-PY-RELEASE-licensing-RELEASE"]}.tar.gz'
pycharm_professional: str = f'pycharm-professional-{products["PC-PY-RELEASE-licensing-RELEASE"]}.tar.gz'

idea_link: str = 'https://download.jetbrains.com/idea/'
pycharm_link: str = 'https://download.jetbrains.com/python/'

home_dir = str(Path.home())
chdir(home_dir)

if ide_number == 1:
    download_jetbrains_ide(idea_link, idea_community)
