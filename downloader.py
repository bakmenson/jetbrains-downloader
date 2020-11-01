#!/usr/bin/env python3

from platform import system
from os import chdir
from pathlib import Path
from subprocess import run
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from sys import exit

from updates_parser import UpdatesParser
from product import Product

req = Request("https://www.jetbrains.com/updates/updates.xml")
MAIN_LINK = "https://download-cf.jetbrains.com"

platform_file_extensions: dict = {
    "Linux": ".tar.gz",
    "Darwin": ".dmg",
    "Windows": ".exe"
}

ide_sublinks = {
    "AppCode": "/objc/AppCode-",
    "CLion": "/cpp/CLion-",
    "DataGrip": "/datagrid/datagrid-",
    "GoLand": "/go/goland-",
    "IntelliJ IDEA Ultimate": "/idea/ideaIU-",
    "IntelliJ IDEA Community": "/idea/ideaIC-",
    "IntelliJ IDEA Edu": "/idea/ideaIE-",
    "PhpStorm": "/webide/PhpStorm-",
    "PyCharm Professional": "/python/pycharm-professional-",
    "PyCharm Community": "/python/pycharm-community-",
    "PyCharm Edu": "/idea/ideaIE-",
    "Rider": "/rider/JetBrains.Rider-",
    "RubyMine": "/ruby/RubyMine-",
    "WebStorm": "/webstorm/WebStorm-",
}

ide_names = [
    "AppCode",
    "CLion",
    "DataGrip",
    "GoLand",
    ("IntelliJ IDEA", ("IntelliJ IDEA Ultimate", "IntelliJ IDEA Community")),
    "PhpStorm",
    ("PyCharm", ("PyCharm Professional", "PyCharm Community")),
    "Rider",
    "RubyMine",
    "WebStorm",
]

updates_parser = UpdatesParser()

try:
    with urlopen(req) as response:
        updates_parser.feed(response.read().decode("utf-8"))

    if not updates_parser.get_product_updates():
        print("\nData not retrieved because <wrong url>.\n")
        exit()

except (HTTPError, URLError) as error:
    print(f"\nData not retrieved because {error}.\n")
    exit()

product_updates = updates_parser.get_product_updates()

platform_system: str = system()

if platform_system != "Darwin":
    ide_sublinks.pop("AppCode")
    product_updates.pop("AppCode")
    ide_names.remove("AppCode")

ide_updates: dict = {}

for ide_name in ide_names:
    for product_name, product_version in product_updates.items():
        if isinstance(ide_name, tuple) and ide_name[0] == product_name:
            ide_updates[ide_name] = product_version
        elif ide_name == product_name:
            ide_updates[ide_name] = product_version

ide = Product()
ide.choose_product(ide_updates)

link = "".join([
    MAIN_LINK,
    ide_sublinks[ide.get_product_name()],
    ide.get_product_version(),
    platform_file_extensions[platform_system]
])

chdir(Path.home())
run("wget " + link, shell=True, check=True)

if platform_system == "Linux":
    downloaded_ide_archive: str = link.split("/")[-1]
    print("Unpacking...")
    run("tar -xf " + downloaded_ide_archive, shell=True, check=True)

print("Done\n")
