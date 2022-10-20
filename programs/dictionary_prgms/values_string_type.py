d = {"a": "hello", "b": 100, "c": 10.1, "d": "world"}
d1 = {}
for key, value in d.items():
    if isinstance(value, str):
        d1[key] = value[::-1]
print(d1)