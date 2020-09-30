#!/usr/bin/env python3


class ChooseIde:

    @classmethod
    def choose_ide(cls, ide_array: tuple) -> str:
        ide_range: int = len(ide_array) + 1

        print()

        for index, ide in enumerate(ide_array):
            print(f"{index + 1:>2}. " + ide + ".")

        print(f"{ide_range}. Exit.")

        cls.ide_name = ide_array[ChooseIde.__choose_integer_in_range(ide_range) - 1]

        return cls.ide_name

    @classmethod
    def __choose_integer_in_range(cls, integer_range: int) -> int:
        while True:
            try:
                cls.ide_number = int(input(">>> "))
            except ValueError:
                print(f"Number most be integer between: 0 - {integer_range}")
                continue

            if 0 < cls.ide_number <= integer_range:
                break

            print(f"Number most be between: 0 - {integer_range}")
            continue

        return cls.ide_number
