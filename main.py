from math import inf, sin, cos
from random import uniform


def randic(dic, f, min):
    pass


def cusrandic(dic, f, cusmin, cusmax, amount=10000):
    for i in amount-1:
        dic[i] = {uniform(cusmin, cusmax), f(uniform(cusmin, cusmax))}


def main():

    def f(x): return ((0.5 * x ** 2) + (5 * sin(x)) + (2 * cos(x) ** 2))
    mini = inf

    which = input("Do you want to find minimum using random values? yes/no")

    if which == 'yes':
        rands = {}

        print('Enter a range for random values to be generated from. ',)
        customrangemin = int(input('Input the minimal value, default is -10 ',) or -10)
        customrangemax = int(input('Input the maximal value, default is 10 ',) or 10)
        print('Random values: {}'.format(rands))
    elif which == 'no':
        pass


if __name__ == '__main__':
    main()
