#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

def my_set():
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = {'red', 'brown'}
    print(input_set.intersection(valid))
    print(input_set.difference(valid))


if __name__ == '__main__':
    my_set()
