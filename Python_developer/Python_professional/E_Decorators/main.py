from decorator import logger
import os

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

PATH = os.path.dirname(os.path.realpath(__file__))


@logger(PATH)
def my_gen(arr):
    for item in arr:
        if isinstance(item, list):
            yield from my_gen(item)
        else:
            yield item


if __name__ == '__main__':
    for item_ in my_gen(nested_list):
        print(item_)
