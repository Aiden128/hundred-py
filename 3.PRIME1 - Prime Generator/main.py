# coding=utf-8
__author__ = 'klein'

# Input
#
# The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.
#
# Output
#
# For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an empty line.

import math

DELMETER = " "


def isPrime(x):
    if x <= 1:
        return False

    # 判斷 2 到 根號 x 之間，是不是有任何數字可以整除 x，有的話就表示這不是質數
    for i in xrange(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def get_input():

    raw = raw_input().strip()

    if DELMETER in raw:
        raws = raw.split(DELMETER)

        if len(raws) == 2 and raws[0].isdigit() and raws[1].isdigit():
            m = int(raws[0])
            n = int(raws[1])

            if 1 <= m <= n <= 1000000000 and (n - m) <= 100000 and n <= 10:
                num = xrange(m, n+1)

                for i in num:
                    if isPrime(i):
                        print i


def main():
    while 1:
        get_input()


if __name__ == "__main__":
    main()