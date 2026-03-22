import utils
import random


def thanos_sort(arr: list[int | float], ascending: bool = True):
    working = arr.copy()
    steps = 0
    while not utils.is_sorted(working, ascending):
        steps += 1
        working = random.sample(working, len(working) // 2)
    return working, steps
