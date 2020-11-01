#!/usr/bin/env python3

from html.parser import HTMLParser


class UpdatesParser(HTMLParser):
    """
    Parser JetBrains products updates

    Attributes:
        __result_data (:obj: `dict` of :key: `str`, :value: `str`):
            key: product name, value: product version.
        __is_allow_take_build_version (bool): by default is false,
            if tag is channel and tag's attribute is -RELEASE-licensing-RELEASE,
            then __is_allow_take_build_version change to true.
        __product_name (str): product name.
        __product_version (str): product version.
    """

    def __init__(self) -> None:
        HTMLParser.__init__(self)
        self.__result_data: dict = {}
        self.__is_allow_take_build_version: bool = False
        self.__product_name: str = ""
        self.__build_version: str = ""

    def get_product_updates(self) -> dict:
        return self.__result_data

    def handle_starttag(self, tag, attrs) -> None:
        if tag == "product":
            self.__product_name = attrs[0][1]

        if tag == "channel":
            if "-RELEASE-licensing-RELEASE" in attrs[0][1]:
                self.__is_allow_take_build_version = True

        if tag == "build" and self.__is_allow_take_build_version:
            self.__build_version = attrs[1][1]
            self.__is_allow_take_build_version = False

            self.__result_data[self.__product_name] = self.__build_version
