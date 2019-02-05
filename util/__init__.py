#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
import random

WILDCAT_POOL_MALE_KEY_LEVEL_1_GROUP = ['wild_male_pool_low', 'wild_male_pool_low_1', 'wild_male_pool_low_2']
WILDCAT_POOL_MALE_KEY_LEVEL_2_GROUP = ['wild_male_pool', 'wild_male_pool_1', 'wild_male_pool_2']
WILDCAT_POOL_FEMALE_KEY_LEVEL_1_GROUP = ['wild_female_pool_low', 'wild_female_pool_low_1', 'wild_female_pool_low_2']
WILDCAT_POOL_FEMALE_KEY_LEVEL_2_GROUP = ['wild_female_pool', 'wild_female_pool_1', 'wild_female_pool_2']

WILDCAT_POOL_MALE_KEY_LEVEL_0 = 'wild_male_pool_init'
WILDCAT_DEMO_POOL_MALE_KEY = 'wild_demo_male_pool'

WILDCAT_POOL_FEMALE_KEY_LEVEL_0 = 'wild_female_pool_init'
WILDCAT_DEMO_POOL_FEMALE_KEY = 'wild_demo_female_pool'


class USER_GENDER(object):
    INIT = 0
    MALE = 1
    FEMALE = 2
    ALL = (MALE | FEMALE)
    GENDERS = {MALE, FEMALE, ALL}
    MALE_FLAGS = ('m', 'M', '男')
    FEMALE_FLAGS = ('f', 'F', '女')


def get_pool_setting():
    low_thres = 50
    male_thres = 300
    female_thres = 2000

    # male/female
    level1 = [random.choice(WILDCAT_POOL_MALE_KEY_LEVEL_1_GROUP),
              random.choice(WILDCAT_POOL_FEMALE_KEY_LEVEL_1_GROUP)]
    level2 = [random.choice(WILDCAT_POOL_MALE_KEY_LEVEL_2_GROUP),
              random.choice(WILDCAT_POOL_FEMALE_KEY_LEVEL_2_GROUP)]

    return [
        [None, low_thres, WILDCAT_POOL_MALE_KEY_LEVEL_0, None, low_thres, WILDCAT_POOL_FEMALE_KEY_LEVEL_0],
        [low_thres, male_thres, level1[0], low_thres, female_thres, level1[1]],
        [male_thres, None, level2[0], female_thres, None, level2[1]]
    ]


def get_wildcat_pool_key(gender, score):
    if gender == USER_GENDER.MALE:
        for each in get_pool_setting():
            if each[0] is not None and score < each[0]:
                pass
            elif each[1] is not None and score > each[1]:
                pass
            else:
                return each[2]
        return WILDCAT_POOL_MALE_KEY_LEVEL_1_GROUP[0]
    else:
        for each in get_pool_setting():
            if each[3] is not None and score < each[3]:
                pass
            elif each[4] is not None and score > each[4]:
                pass
            else:
                return each[5]
        return WILDCAT_POOL_FEMALE_KEY_LEVEL_1_GROUP[0]


def test():
    params = [
        (992, 49),
        (6164471, 160.1),
        (84044424, 133.74),
        (94286258, 4914.35),
        (28063005, 6913.82),
        (4917222, 530.74),
        (991, 50),
        (993, 3000)
    ]
    for param in params:
        uid, score = param
        print uid, get_wildcat_pool_key(2, score)


if __name__ == '__main__':
    test()
