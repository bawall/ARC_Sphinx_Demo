# a small main programme
# use features.py
# use classes.py
import sys


def main():
    arg = sys.argv
    print('Hello World - main - begin')
    print('Arguments: {arg}'.format(arg=arg))

    print('Hello World - main - end')


if __name__ == '__main__':
    main()
