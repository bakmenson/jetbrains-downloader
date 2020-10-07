#!/usr/bin/env python3


class IDE:

    def __init__(self, products: Union[list, tuple]) -> None:
        self.__products: Union[list, tuple] = products
        self.__products_with_index: dict = {}
        self.__product_name: str = ""
        self.__index: int = 0

    def get_ide(self) -> dict:
        return self.__ide

    def choose_ide(self):
        self.__print_ide_names()
        self.__ide_number = self.__choose_integer_in_range()
        self.__ide_version = self.__ide_names[self.__ide_number][-1]

        if isinstance(self.__ide_names[self.__ide_number][0][1], tuple):
            self.__ide_names = self.__set_index_for_ide_name(
                self.__ide_names[self.__ide_number][0][1]
            )

            self.__print_ide_names()
            self.__ide_number = self.__choose_integer_in_range()
            self.__ide_name = self.__ide_names[self.__ide_number]

        else:
            self.__ide_name = self.__ide_names[self.__ide_number][0]

        self.__ide[self.__ide_name] = self.__ide_version

    def __print_ide_names(self):
        print()

        for key, value in self.__ide_names.items():
            if isinstance(value, str):
                print(f"{key:>2}. " + value)
            elif isinstance(value[0], str):
                print(f"{key:>2}. " + value[0])
            else:
                print(f"{key:>2}. " + value[0][0])

        print(f"{len(self.__ide_names.keys()) + 1:>2}. Exit.")

    def __choose_integer_in_range(self) -> int:
        number = 0
        number_range = len(self.__ide_names) + 1

        while True:
            try:
                number = int(input(">>> "))
            except ValueError:
                print(f"Number most be integer between: 0 - {number_range}")
                continue

            if 0 < number <= number_range:
                break

            print(f"Number most be between: 0 - {number_range}")
            continue

        return number

    def __set_index_for_ide_name(self, ide_names) -> dict:
        ide_name_with_index: dict = {}

        for index, item in enumerate(ide_names, start=1):
            ide_name_with_index[index] = item

        return ide_name_with_index
