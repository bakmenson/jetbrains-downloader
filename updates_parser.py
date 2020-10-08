#!/usr/bin/env python3

from html.parser import HTMLParser


class UpdatesParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__result_data = {}
        self.__is_allow_take_build_version = False
        self.__product_name: str = ""
        self.__build_version: str = ""

    def get_product_updates(self):
        return self.__result_data

    def handle_starttag(self, tag, attrs):
        if tag == "product":
            self.__product_name = attrs[0][1]

        if tag == "channel":
            if "-RELEASE-licensing-RELEASE" in attrs[0][1]:
                self.__is_allow_take_build_version = True

        if tag == "build" and self.__is_allow_take_build_version:
            self.__build_version = attrs[1][1]
            self.__is_allow_take_build_version = False

            self.__result_data[self.__product_name] = self.__build_version
