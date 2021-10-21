# https://projecteuler.net/problem=9
import math


def pythagorean_sum(a: int, b: int) -> float:
    return a ** 2 + b ** 2


def sqrt_integer(a: int, b: int) -> bool:

    total_sum = pythagorean_sum(a, b)
    return math.sqrt(total_sum).is_integer()


def test_integer_sum(a: int, b: int, c: int) -> bool:
    return a + b + c == 1000


def main():

    a = 1
    b = 2

    while True:
        if sqrt_integer(a, b) and test_integer_sum(
            a, b, int(math.sqrt(pythagorean_sum(a, b)))
        ):
            print(
                f"Your ~~1000~~ pythagorean numbers are {a}\N{SUPERSCRIPT TWO} + {b}\N{SUPERSCRIPT TWO} = {int(math.sqrt(pythagorean_sum(a, b)))}\N{SUPERSCRIPT TWO}"
            )
            print(
                f"Your pythagorean product is {a * b * int(math.sqrt(pythagorean_sum(a, b)))}"
            )
            break
        else:
            if sqrt_integer(a, b):
                print(
                    f"Square Root Integer - {a}\N{SUPERSCRIPT TWO} + {b}\N{SUPERSCRIPT TWO} = {int(math.sqrt(pythagorean_sum(a, b)))}\N{SUPERSCRIPT TWO}"
                )

            if a > 1000:
                print("You didn't find the product")
                break
            elif a + b + math.sqrt(pythagorean_sum(a, b)) > 1000:
                a += 1
                b = a + 1
            else:
                b += 1


if __name__ == "__main__":
    main()
