#!./python

from itertools import groupby, islice

#from itertools import all_equal as itertools_all_equal
def take(n, iterable):
    '''
    https://more-itertools.readthedocs.io/en/stable/_modules/more_itertools/recipes.html#take
    '''
    return list(islice(iterable, n))

def itertools_all_equal_1(iterable, key=None):
    '''
    https://docs.python.org/3/library/itertools.html
    '''
    "Returns True if all the elements are equal to each other."
    return len(take(2, groupby(iterable, key))) <= 1

def itertools_all_equal_2(iterable):
    '''
    https://more-itertools.readthedocs.io/en/stable/_modules/more_itertools/recipes.html#all_equal
    '''
    """
    Returns ``True`` if all the elements are equal to each other.

        >>> all_equal('aaaa')
        True
        >>> all_equal('aaab')
        False

    """
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def baseline(iterable):
    for _ in iterable:
        pass


def example_calls():

    input_list = [1, 1, 1]
    input_list = []
    print(all_equal(input_list))

    print(itertools_all_equal_1(input_list))
    print(itertools_all_equal_2(input_list))


from time import time
def main():

    iterable = [1] * 10**8 + [2]

    candidate_functions = [
        baseline,
        all_equal,
        itertools_all_equal_1,
        itertools_all_equal_2,
    ]

    for _ in range(5):
        for f in candidate_functions:
            t0 = time()
            print(f(iterable), f'{(time()-t0)*1e3:.1f} ms ', f.__name__)
        print(f'')


if __name__ == '__main__':
    main()
