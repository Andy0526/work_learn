#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

from util.excel_util import Excel


def main():
    excel = Excel()
    fields = ['字段1', '字段2']
    excel.create_sheet(fields, sheet_name='日报')
    excel.add_row(['test1_1', 'test1_2'])
    excel.add_row(['test1_1', 'test1_2'])
    excel.create_sheet(fields, sheet_name='周报')
    excel.add_row(['test2_1', 'test2_2'])
    excel.add_row(['test2_1', 'test2_2'])
    excel.create_sheet(fields, sheet_name='月报')
    excel.add_row(['test3_1', 'test3_2'])
    excel.add_row(['test3_1', 'test3_2'])
    excel.save(u'测试.xls')


if __name__ == '__main__':
    main()
