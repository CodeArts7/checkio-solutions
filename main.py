def mult_two(a: int, b: int) -> int:
    # just a multiplication of two initial numbers using "*" sign
    return a * b


if __name__ == "__main__":
    print("Result:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
