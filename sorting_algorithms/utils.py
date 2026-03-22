def is_sorted(arr: list[int | float], ascending: bool = True):
    if ascending:
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    else:
        return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
