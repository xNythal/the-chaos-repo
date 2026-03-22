import ast
from typing import Any


def manual_sort(arr: list[Any], ascending: bool = True) -> list[Any]:
    try:
        return ast.literal_eval(input("Please sort the array Mr. Human: "))
    except:
        print("What've you done Mr. Human?!")
        return []
