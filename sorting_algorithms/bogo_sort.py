import utils
import random


def bogo_sort(arr: list[int | float], ascending: bool = True):
    working = arr.copy()
    attempts = 0
    while not utils.is_sorted(working, ascending):
        random.shuffle(working)
        attempts += 1
    return working, attempts
