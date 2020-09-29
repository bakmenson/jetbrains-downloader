#!/usr/bin/env python3


class ChooseIde:

    @staticmethod
    def choose_ide(ide_array: tuple) -> str:
        ide_range: int = len(ide_array) + 1

        print()

        for index, ide in enumerate(ide_array):
            print(f"{index + 1}. " + ide + ".")

        print(f"{ide_range}. Exit.")

        ide_number = ChooseIde.__choose_integer_in_range(ide_range)

        return list(ide_array)[ide_number - 1]

    @staticmethod
    def __choose_edition():
        pass

    @staticmethod
    def __choose_integer_in_range(integer_range: int) -> int:
        while True:
            try:
                number = int(input(">>> "))
            except ValueError:
                print(f"Number most be integer between: 0 - {integer_range}")
                continue

            if 0 < number <= integer_range:
                break

            print(f"Number most be between: 0 - {integer_range}")
            continue

        return number
