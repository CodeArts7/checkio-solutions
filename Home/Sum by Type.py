from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    words = ''
    numbers = 0
    for i in items:
        if type(i) is str:
            words += i
        elif type(i) is int:
            numbers += i
    return words, numbers


if __name__ == "__main__":
    print("Example:")
    print(sum_by_types([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")