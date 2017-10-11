#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import re
import xlwt

def create_workbook():
    workbook = xlwt.Workbook(encoding='utf-8')
    return workbook


def add_sheet_row(worksheet, values, row_index=0):
    for col, value in enumerate(values):
        worksheet.write(row_index, col, value)


def create_sheet(workbook, fields, sheet_name='sheet1'):
    worksheet = workbook.add_sheet(sheet_name)
    add_sheet_row(worksheet, fields)
    return worksheet


def save_workbook(workbook, file_name=None):
    workbook.save(file_name)
    return file_name

class Excel(object):

    POSTFIX = '_副本'
    R = re.compile(r'%s(\d+)' % POSTFIX)

    def __init__(self):
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet = None
        self.row_index = 0
        self.sheet_index = -1
        self.sheets = []

    def create_sheet(self, fields, sheet_name='sheet1'):
        self.worksheet = self.workbook.add_sheet(sheet_name)
        self.row_index = 0
        if len(self.sheets) > 0:
            info = self.sheets[-1]
            info['row_count'] = min(0, self.row_index - 1)
        self.sheets.append({'fields': fields, 'sheet_name': sheet_name, 'row_count': 0})
        self.add_row(fields)

    def add_row(self, values):
        if self.worksheet is None:
            return
        if not values:
            return
        for col, value in enumerate(values):
            self.worksheet.write(self.row_index, col, value)
        self.row_index += 1

    def save(self, file_name=None):
        self.workbook.save(file_name)
        return file_name

    def get_index(self):
        return self.row_index

    def copy_sheet(self, sheet_name=None):
        if self.sheets:
            info = self.sheets[-1]
            if sheet_name is None:
                sheet_name = info['sheet_name']
                m = Excel.R.search(sheet_name)
                index = 1
                if m:
                    index = int(m.group(1)) + 1
                sheet_name += '%s%s' % (Excel.POSTFIX, index)
            self.create_sheet(fields=info['fields'], sheet_name=sheet_name)
