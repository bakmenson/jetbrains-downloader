#!/usr/bin/env python3

from html.parser import HTMLParser


class JetbrainsUpdatesParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__result_data = {}
        self.__is_able_take_build_version = False
        self.__product_id: str = ""

    def get_result_data(self):
        return self.__result_data

    def handle_starttag(self, tag, attrs):
        if tag == "channel":
            self.__product_id = attrs[0][1]
            self.__is_able_take_build_version = True

        if tag == "build" and self.__is_able_take_build_version:
            self.__result_data[self.__product_id] = attrs[1][1]
            self.__is_able_take_build_version = False
