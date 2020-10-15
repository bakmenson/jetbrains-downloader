#!/usr/bin/env python3

from platform import system
from urllib.request import Request

from updates_parser import UpdatesParser
from products import Products
from download_link import DownloadLink
from downloader_utility import download_ide, parser_feed, get_ide_updates, \
        extract_tar_archive

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

parser_feed(updates_parser, req)

product_updates = updates_parser.get_product_updates()

platform_system: str = system()

if platform_system != "Darwin":
    ide_sublinks.pop("AppCode")
    product_updates.pop("AppCode")
    ide_names.remove("AppCode")

ide_updates: dict = get_ide_updates(ide_names, product_updates)

products = Products(ide_updates)
products.choose_product()

ide: dict = products.get_product()

download_link = DownloadLink(MAIN_LINK, ide_sublinks,
                             platform_file_extensions[platform_system], ide)

link = download_link.get_download_link()

download_ide(link)

if platform_system == "Linux":
    downloaded_ide_archive: str = link.split("/")[-1]
    extract_tar_archive(downloaded_ide_archive)

print("Done\n")
