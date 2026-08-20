from typing import Any
def all_unique(items: list[Any]) -> bool:
    items_set = set(items)
    return len(items) == len(items_set)

def driver():
    items = ["red", "blue", "yellow", "green", "orange"]
    res = all_unique(items)
    print(res)