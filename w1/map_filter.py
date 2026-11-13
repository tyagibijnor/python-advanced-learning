numbers = [1, 2, 3, 4, 5]

## The map() function applies a given function to every element in an iterable.
result = list(map(lambda x: x * 2, numbers))

print(result)

numbers = [10, 15, 20, 25, 30, 35]

## The filter() function selects elements based on a condition.
result = list(filter(lambda x: x > 20, numbers))

print(result)