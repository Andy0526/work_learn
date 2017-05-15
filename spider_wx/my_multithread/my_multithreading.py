#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
import random
from multiprocessing import Pool

import time


def _thread_op(s_file):
    with open(s_file, 'w') as f:
        f.write('test...')
        seconds = random.random() * 5
        time.sleep(seconds)
        print s_file, seconds
    return '{} finished'.format(s_file)


if __name__ == '__main__':
    begin = time.time()
    size = 5
    pool = Pool(5)
    files = ['test_{}'.format(idx) for idx in range(5)]
    print 1
    # res = [_thread_op(s_file) for s_file in files]
    res = pool.map(_thread_op, files)
    print 2
    print 'run_time: {} res:{}'.format(time.time() - begin, res)
    pool.close()
    pool.join()
    print 'run_time: {} res:{}'.format(time.time() - begin, res)
