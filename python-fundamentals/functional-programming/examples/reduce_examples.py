

from functools import reduce

##The reduce() function combines iterable elements into a single result.
## It is available in the functools module.

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)