import time
import utils


def miracle_sort(arr: list[int | float], ascending: bool = True):
    attempts = 0
    while not utils.is_sorted(arr, ascending):
        time.sleep(5)
        attempts += 1

    return arr, attempts
