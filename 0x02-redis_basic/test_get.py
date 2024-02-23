#!/usr/bin/env python3
Cache = __import__('exercise').Cache
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    r_value = cache.get(key, fn=fn)
    print(f"key: {key},\tvalue: {value}\tr_value: {r_value}")
    assert r_value == value

print(cache.get('hello', None))
