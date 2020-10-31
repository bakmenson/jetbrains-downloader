#!/usr/bin/env python3

from typing import Union
from sys import exit


class Products:
    """
    JetBrains products

    Args:
        products (:obj: `dict` of :key: `str`, :value: `str`):
            key is product name, value is product version.

    Attributes:
        __products (Union[:obj: `dict` of :key: `str`, :value: `str`,
                          :obj: `tuple` of `str`]):
            products names and versions if dict
            or products names if tuple.
        __products_with_index (:obj: `dict` of :key: `int`, :value: `dict`):
            key is number of product,
            value is product (name: version).
        __product_name (str): product name.
        __product_version (str): product version.
        __index (int): product index of __products_with_index.
    """

    def __init__(self, products: dict) -> None:
        self.__products: Union[dict, tuple] = products
        self.__products_with_index: dict = {}
        self.__product_name: str = ""
        self.__product_version: str = ""
        self.__index: int = len(self.__products) + 1

    def get_product(self) -> dict:
        return {self.__product_name: self.__product_version}

    def choose_product(self) -> None:
        self.__choose_product_index()
        self.__product_version = self.__products_with_index[self.__index][1]

        if isinstance(self.__products_with_index[self.__index][0], tuple):
            self.__products = self.__products_with_index[self.__index][0][1]
            self.__choose_product_index()
            self.__product_name = self.__products_with_index[self.__index]
        else:
            self.__product_name = self.__products_with_index[self.__index][0]

    def __choose_product_index(self) -> None:
        self.__set_products_indexes()
        self.__print_products()
        self.__choose_index()

        if self.__index == len(self.__products_with_index) + 1:
            exit()

    def __set_products_indexes(self) -> None:
        self.__products_with_index.clear()
        if isinstance(self.__products, dict):
            for index, item in enumerate(self.__products.items(), start=1):
                self.__products_with_index[index] = item
        else:
            for index, item in enumerate(self.__products, start=1):
                self.__products_with_index[index] = item

    def __print_products(self) -> None:
        for key, value in self.__products_with_index.items():
            if isinstance(value[0], tuple):
                print(f"{key:>2}. {value[0][0]}")
            elif isinstance(value, tuple):
                print(f"{key:>2}. {value[0]}")
            else:
                print(f"{key:>2}. {value}")
        print(f"{len(self.__products_with_index) + 1:>2}. Exit.")

    def __choose_index(self) -> int:
        index_range = len(self.__products_with_index) + 1

        while True:
            try:
                self.__index = int(input(">>> "))
            except ValueError:
                print(f"Number most be integer between: 0 - {index_range}")
                continue

            if 0 < self.__index <= index_range:
                break

            print(f"Number most be between: 0 - {index_range}")
            continue

        return self.__index
