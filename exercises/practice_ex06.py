a: dict[str, str] = {}
a = {'a': 'z', 'b': 'x', 'c': 'x'}
result: dict[str, str] = {}
result: dict[str, str] = {}
for x in a:
    result[a[x]] = x
    if result[x] == a[x]: 
        raise KeyError  # could be cleaner. Why is the message longer than the example?
print(result)