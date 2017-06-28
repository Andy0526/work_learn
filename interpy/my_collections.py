#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

from collections import defaultdict, Counter, deque, namedtuple



def _defaultdict():
    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )
    favourite_colours = defaultdict(list)
    print favourite_colours
    for name, colour in colours:
        favourite_colours[name].append(colour)
    print(favourite_colours)


def _counter():
    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )
    favs = Counter(name for name, _ in colours)
    print(favs)


def _deque():
    d = deque()
    d.append('1')
    d.append('2')
    d.append('3')
    print len(d), d, d[0], d[-1]
    print d.popleft(), d.pop()
    print len(d), d, d[0], d[-1]


def _namedtuple():
    Animal = namedtuple('Animal', 'name age type')
    print Animal, Animal.__doc__
    perry = Animal(name="perry", age=31, type="cat")
    print perry
    perry._replace(age=42)
    print perry


if __name__ == '__main__':
    # _defaultdict()
    # _counter()
    # _deque()
    _namedtuple()
