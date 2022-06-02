import sys


def print_hi(name, ARGone, ARGtwo):
    print(f'Hi, {name}')
    print(f'Args: URL: {ARGone}, Depth: {ARGtwo}')


if __name__ == '__main__':
    # TODO: Add here calling for external library facade with argv as list (validation flow is in inner logic)
    print_hi('PyCharm', sys.argv[1], sys.argv[2])
