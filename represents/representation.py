# -*- coding: utf-8 -*-
# MIT License

# Copyright (c) 2021 Arthur

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Any

max_str_length = 20


def set_max_str_length(new_length: int):
    """
    Sets the length before the ellipsis effect should occur on strings.
    0 = infinite/no ellipsis

    Args:
        new_length (int): The new ellipsis length.
    """
    global max_str_length
    max_str_length = new_length + 5


def represents(obj: object) -> str:
    """
    Creates a string representing of an object.

    Args:
        obj (object): The object (class) that should be represented.
    Returns:
        str: A correct representation of the object including the object parameters.
    """

    def process(item: Any):
        item = f"'{item}'" if isinstance(item, str) else item
        if issubclass(item.__class__, Represents):
            item = repr(item)
        elif 4 < max_str_length < len(item) and isinstance(item, str):
            item = item[0:max_str_length - 4] + "'..."

        return item

    items = [i for i in vars(obj).items() if not i[0].startswith("_")]
    return f"<{obj.__class__.__name__}{' ' if len(items) > 0 else ''}{' '.join(list(map(lambda p: f'{p[0]}={process(p[1])}', items)))}>"


class Represents:
    """Handles representations for classes"""
    __repr__ = represents


def represents_decorator(cls):
    cls.__repr__ = represents
    return cls
