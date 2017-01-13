from math import inf, sin, cos
from random import uniform
import matplotlib.pyplot as plt


def randic(dic, f, min):
    pass


def cusrandic(dic, f, cusmin, cusmax, amount=20000):
    for i in range(amount):
        randnum = uniform(cusmin, cusmax)
        if randnum not in dic.items():
            dic[randnum] = f(randnum)
        else:
            amount += 1


def findmin(dic):
    mini = [inf]
    for i in dic:
        if dic[i] < mini[0]:
            mini = []
            mini.append(dic[i])
        elif dic[i] == mini[0]:
            mini.append(dic[i])
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
        minimum = findmin(rands)

        # for i in rands:
        #     print(rands[i])

        print('minimum:', minimum)
        fx = [x/10**3 for x in range(customrangemin*(10**3), customrangemax*(10**3))]

        plt.plot(fx, [f(x) for x in fx], [x for x, y in rands.items() if y == minimum[0]], [minimum], 'ro')
        plt.show()

    elif which == 'no':
        pass


if __name__ == '__main__':
    main()
