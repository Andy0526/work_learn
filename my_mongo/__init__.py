# -*- coding: utf-8 -*-
def get_products():
    l = []
    print('请输入内容，以逗号隔开【单独输入\':q\'保存退出】')
    while True:
        products = []
        content = input()
        if content == 'q':
            break
        a, b, c = content.split(',')
        products.append(a)
        products.append(b)
        products.append(c)
        l.append(products)
    return l


def by_id(l):
    return int(l[0])


def by_name(l):
    return l[1]


def by_price(l):
    return float(l[2])


def get_sorted_products(l, args):
    if args == 'id':
        return sorted(l, key=by_id)
    elif args == 'name':
        return sorted(l, key=by_name)
    elif args == 'price':
        return sorted(l, key=by_price)
    else:
        print("输入内容不合法")


##验证方法
L1 = get_products()  ##得到输入的信息
L2 = get_sorted_products(L1, 'id')  ##按照id排序
L3 = get_sorted_products(L1, 'name')  ##按照name排序
L4 = get_sorted_products(L1, 'price')  ##按照price排序
