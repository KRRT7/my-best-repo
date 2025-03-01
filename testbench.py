from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool



def add_numbers(a,b):
    return a+b


def function1():
    pool = ThreadPoolExecutor(max_workers=None)
    numbers = [(1,2), (3,4), (5,6)]
    result = pool.map(add_numbers, *zip(*numbers))

    for r in result:
        print(r)

def function2():


    pool = Pool()
    numbers = [(1,2), (3,4), (5,6)]
    result = pool.starmap(add_numbers, numbers)
    pool.close()
    pool.join()

    for r in result:
        print(r)

def function3( a, b):
    return a+b
if __name__ == "__main__":

    function1()
    function2()
    function3(1, 2)


