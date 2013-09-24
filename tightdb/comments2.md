# Comments round two

## In the Python interpreter

Wanted to try inserting a lot of records in the Python shell. That creates a lot of screen prints and takes almost an hour!

```
$ python
>>> import tightdb, string, random
>>> randword = lambda n: "".join([random.choice(string.letters) for i in range(n)])
>>> t = tightdb.Table(["name", "string", "age", "int"])
>>> for i in range(1000000):
...   t.append([randword(10), random.randint(100,999)])
>>> #
```

