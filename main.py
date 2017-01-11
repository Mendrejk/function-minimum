from math import inf, sin, cos
from random import uniform


def randic(dic, f, min):
    pass


def cusrandic(dic, f, cusmin, cusmax, amount=500):
    for i in range(amount):
        randnum = uniform(cusmin, cusmax)
        if randnum not in dic.items():
            dic[randnum] = f(randnum)
        else:
            amount += 1


def findmin(dic):
    mini = inf
    for i in dic:
        if dic[i] < mini:
            mini = dic[i]
    return mini


def f(x): return ((0.5 * x ** 2) + (5 * sin(x)) + (2 * cos(x) ** 2))


def main():
    which = input("Do you want to find minimum using random values? yes/no ")

    if which == 'yes':
        rands = {}

        print('Enter a range for random values to be generated from. ',)
        customrangemin = int(input('Input the minimal value, default is -10 ',) or -10)
        customrangemax = int(input('Input the maximal value, default is 10 ',) or 10)
        cusrandic(rands, f, customrangemin, customrangemax)
        print('Random values: {}'.format(rands))
        # for i in rands:
        #     print(rands[i])
        print('mini:', findmin(rands))
    elif which == 'no':
        pass


if __name__ == '__main__':
    main()
