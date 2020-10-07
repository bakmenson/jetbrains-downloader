#!/usr/bin/env python3

from typing import Union
from sys import exit


class IDE:

    def __init__(self, products: Union[list, tuple]) -> None:
        self.__products: Union[list, tuple] = products
        self.__products_with_index: dict = {}
        self.__product_name: str = ""
        self.__index: int = 0

    def get_product_name(self) -> str:
        return self.__product_name

    def choose_product(self) -> None:
        self.__choose_product()

        if isinstance(self.__products_with_index[self.__index], tuple):
            self.__products = self.__products_with_index[self.__index][1]
            self.__choose_product()

        self.__product_name = self.__products_with_index[self.__index]

    def __choose_product(self) -> None:
        self.__set_index_for_products()
        self.__print_products()
        self.__choose_index()

        if self.__index == len(self.__products_with_index) + 1:
            exit()

    def __set_index_for_products(self) -> None:
        self.__products_with_index.clear()
        for index, item in enumerate(self.__products, start=1):
            self.__products_with_index[index] = item

    def __print_products(self) -> None:
        for key, value in self.__products_with_index.items():
            if isinstance(value, tuple):
                print(f"{key:>2}. {value[0]}")
            else:
                print(f"{key:>2}. {value}")
        print(f"{len(self.__products_with_index) + 1:>2}. Exit.")

    def __set_index_for_ide_name(self, ide_names) -> dict:
        ide_name_with_index: dict = {}

        for index, item in enumerate(ide_names, start=1):
            ide_name_with_index[index] = item

        return ide_name_with_index
