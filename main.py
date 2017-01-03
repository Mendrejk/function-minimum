from math import inf, sin, cos
from random import uniform


def main():

    mini = inf
    which = bool(input("Do you want to find minimum using random values?"))

    def f(x): return ((0.5 * x ** 2) + (5 * sin(x)) + (2 * cos(x) ** 2))

    if which:
        print("Enter a range for random values to be generated from.", end='')


if __name__ == '__main__':
    main()
