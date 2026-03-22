import threading
import time
from typing import Sequence


def sleep_sort(arr: Sequence[int | float], max_delay: float = 0.1):
    result: list[int | float] = []

    max_val = max(arr)
    scale = max_delay / max_val if max_val > 0 else 1

    def sleeper(x: int | float):
        time.sleep(x * scale)
        result.append(x)

    threads = [threading.Thread(target=sleeper, args=(x,)) for x in arr]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return result
