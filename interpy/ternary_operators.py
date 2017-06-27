#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

def ternary_operators():
    is_fat = True
    state = "fat" if is_fat else "not fat"
    print state
    fat = True
    fitness = ("skinny", "fat")[fat]
    print("Ali is ", fitness)


if __name__ == '__main__':
    ternary_operators()
