# -*- coding: utf-8 -*-
# !/usr/bin/env python

def words_traverse(words_list):
    if not words_list:
        return []
    route_list = words_list[0]
    for words in words_list[1:]:
        temp_routes = []
        for route in route_list:
            temp_routes.extend("{} {}".format(route, word) for word in words)
        route_list = temp_routes
    return route_list


if __name__ == '__main__':
    words_list = [['shui3'], ['guo3', 'luo3', 'guan4'], ['1', '2']]
    print(words_traverse(words_list))
