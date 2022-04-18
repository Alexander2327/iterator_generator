def flat_generator(gen_list):
    for itm in gen_list:
        if isinstance(itm, list):
            for i in flat_generator(itm):
                yield i
            # yield from flat_generator(itm)
        else:
            yield itm


nested_list = [
    ['a', [1, [4, 7, 8]], 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

for item in flat_generator(nested_list):
    print(item)
