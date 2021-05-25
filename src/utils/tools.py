from itertools import tee, islice, chain

def previous_and_next(some_iterable):
    '''CC BY-SA 3.0 https://stackoverflow.com/a/1012089'''

    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)
