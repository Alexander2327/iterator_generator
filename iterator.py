class FlatIterator:
    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.len_list = len(self.iter_list)
        self.cursor = -1
        self.n_cursor = -1

    def __iter__(self):
        self.cursor += 1
        self.n_cursor += 1
        return self

    def __next__(self):
        if self.n_cursor == len(self.iter_list[self.cursor]):
            self.cursor += 1
            self.n_cursor = 0
        if self.cursor == self.len_list:
            raise StopIteration
        self.n_cursor += 1
        return self.iter_list[self.cursor][self.n_cursor - 1]


nested_list = [
    ['a', [1, 5], 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
