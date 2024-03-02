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


'''debug build
None 912.4 ms  baseline
False 833.9 ms  all_equal
False 1229.8 ms  itertools_all_equal_1
False 1264.8 ms  itertools_all_equal_2

None 1097.5 ms  baseline
False 850.6 ms  all_equal
False 1207.6 ms  itertools_all_equal_1
False 1210.2 ms  itertools_all_equal_2

None 1059.9 ms  baseline
False 838.3 ms  all_equal
False 1220.5 ms  itertools_all_equal_1
False 1238.5 ms  itertools_all_equal_2

None 1066.1 ms  baseline
False 858.0 ms  all_equal
False 1230.9 ms  itertools_all_equal_1
False 1215.4 ms  itertools_all_equal_2

None 1065.1 ms  baseline
False 840.4 ms  all_equal
False 1252.0 ms  itertools_all_equal_1
False 1240.2 ms  itertools_all_equal_2
'''