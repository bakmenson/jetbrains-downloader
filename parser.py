#!/usr/bin/env python3

from html.parser import HTMLParser


class IDENamesParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__ide_names = []
        self.__is_taken_ide_name = True
        self.__is_ide_attr = False
        self.__ide_attrs = ("ide", "ide,data-science")

    def get_names(self):
        return self.__ide_names

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[1] in self.__ide_attrs:
                self.__is_ide_attr = True
            if self.__is_ide_attr and attr[1] == "product-item__title-link":
                self.__is_ide_attr = False
                self.__is_taken_ide_name = False

    def handle_data(self, data):
        if not self.__is_taken_ide_name:
            self.__ide_names.append(data)
            self.__is_taken_ide_name = True


class IDEUpdatesParser(HTMLParser):

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
