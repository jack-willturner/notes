# Why are they called Key, Value, and Query?

These are my notes on the Key, Value, Query vectors/matrices in attention. In particular, it took me a while to understand why they were called Key, Value, and Query.

**Disclaimer** - this isn't at all how Python dictionaries work. But I'm going to be extremely liberal with my handwavey interpretation of how they *could* be implemented.

Imagine we have a Python dictionary:

```python
numbers = {
  0: 'zero',
  1: 'one',
  ...
  d : "d"
}
```

Each row is a pair which maps a `key` to a `value` (e.g. the key `0` maps to the value `'zero'`).

When we index into the dictionary, we do:

```python
numbers[1]
```

In some sense, we are passing in a `query` that says: find the key that corresponds to the hash of `1`.

**trigger warning**: not at all how Python dictionaries work.

You could image this being written:

```python
def f(query, key):
  if query == key:
    return 1
  else:
    return 0
```

Now we loop over each of the keys and we compute f, resulting in a vector:

$$
v =
$$

Where each item in the vector tells us whether this is the index we want.

What if instead, `f` returned a continuous value? E.g. Instead of checking whether the
number **is** 1, why don't we check if it's *close* to 1:

**trigger warning**: division by zero.

```python
def f(query, key):
  return 1 / abs(query-key)
```
