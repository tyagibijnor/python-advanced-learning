## Basic Iterator
def basic_iter(emp):
    emp  = iter(emp)
    while True:
        try:
            print(next(emp))
        except StopIteration:
            break