## Exercise 1 — Make Multiplier
def make_multiplier(factor):

    def multiply(val):
        return factor * val

    return multiply


## Excercise 2
def make_counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
