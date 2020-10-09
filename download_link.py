#!/usr/bin/env python3


class DownloadLink:

    def __init__(self,
                 main_link: str,
                 sublinks: dict,
                 file_extension: str,
                 product: dict) -> None:

        self.__sublinks: dict = sublinks
        self.__file_extinsion: str = file_extension
        self.__product = product
        self.__download_link: str = main_link + self.__product_link()

    def get_download_link(self) -> str:
        return self.__download_link

    def __product_link(self) -> str:
        link: str = ""

        for name, sublink in self.__sublinks.items():
            if name == tuple(self.__product)[0]:
                link += sublink + self.__product[name]

        link += self.__file_extinsion

        return link
