nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def my_gen(arr):
    for item in arr:
        if isinstance(item, list):
            yield from my_gen(item)
        else:
            yield item


class FlatIterator:
    def __init__(self, i_list):
        self.i_list = sum(i_list, [])

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.i_list):
            raise StopIteration
        return self.i_list[self.cursor]


flat_list = [item for item in FlatIterator(nested_list)]

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    print('')
    print(flat_list)
    print('')
    for item in my_gen(nested_list):
        print(item)
