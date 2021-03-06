# Represents library

A utility library created to easily make great looking `__repr__` classes without effort!
This library is also supports recursive class inheritance, for previously inherited classes.

## Installation

You can easily install the library from PyPi by using `pip`.
```bash
pip install represents
```

## Supported methods:

### Class decorator:

```python
from represents import represents_decorator


@represents_decorator
class MyClass:
    pass
```

### Class inheritance:

```python
from represents import Represents


class Foo(Represents):
    pass
```

### Manual:

```python
from represents import represents


class Foo:
    __repr__ = represents
```

## Responses:

* **Empty object**: `<ObjectName>`
* **Object**: `<ObjectName string='value' amount=123 bool=True>`
* **Recursive object**: `<ObjectName foo='foo' sub_obj=<SecondObject bar='bar'>>`

# Examples

Examples can be found @ [the github examples directory](https://github.com/Arthurdw/Represents/tree/master/examples)
