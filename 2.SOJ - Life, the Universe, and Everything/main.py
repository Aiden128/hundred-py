__author__ = 'klein'

# Input:
# 1
# 2
# 88
# 42
# 99
#
# Output:
# 1
# 2
# 88

STAND_FOR_INT = 1

def get_input():

    while 1:
        n = raw_input()

        if n.isdigit():
            if int(n) != 42:
                print n
            else:
                break


def main():
    get_input()


if __name__ == "__main__":
    main()