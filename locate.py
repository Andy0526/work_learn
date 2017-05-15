#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import geoutil
import sys
import re

i_precision = 0
locations = {}

pos_pattern = re.compile(r'geo:(.*?) location', re.S)

location_pattern = re.compile(r'location:\((.*?)\)"}', re.S)


def get_location_info(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            try:
                s_pos = re.search(pos_pattern, line).group(1)
                s_location = re.search(location_pattern, line).group(1)
                pos_1, pos_2 = s_pos.split(',')
                locations[(float(pos_1), float(pos_2))] = s_location
            except Exception:
                continue


def check_location():
    # with open('check_location_{}.log'.format(i_precision), 'a') as f:
        # for pos_1, pos_2 in locations.keys()[:500]:
        for pos_1, pos_2 in [(18.796231, 98.963161)]:
            fix_pos_1 = round(pos_1, i_precision)
            fix_pos_2 = round(pos_2, i_precision)
            res_1 = geoutil.GeoUtil.get_locations('{},{}'.format(pos_1, pos_2))
            res_2 = geoutil.GeoUtil.get_locations('{},{}'.format(fix_pos_1, fix_pos_2))
            print res_1, res_2
            # if res_1 != res_2:
                # f.write('pos:{},{},location:{}  ;   fixed_pos:{},{},location:{}\n'.format(pos_1, pos_2, ','.join(res_1),
                #                                                                           fix_pos_1, fix_pos_2,
                #                                                                           ','.join(res_2)))
                # f.flush()


def main():
    get_location_info('geo')
    check_location()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        i_precision = int(sys.argv[1])
    else:
        i_precision = 2
    main()
