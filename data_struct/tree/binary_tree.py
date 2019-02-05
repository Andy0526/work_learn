# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if not treeNode.lchild:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)

    def front_traverse(self, root):
        if not root:
            return
        print root.elem
        self.front_traverse(root.lchild)
        self.front_traverse(root.rchild)

    def middle_traverse(self, root):
        if not root:
            return None
        self.middle_traverse(root.lchild)
        print root.elem
        self.middle_traverse(root.rchild)

    def later_traverse(self, root):
        if not root:
            return
        self.later_traverse(root.lchild)
        self.later_traverse(root.rchild)
        print root.elem

    def front_traverse_by_stack(self, root):
        if not root:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                print node.elem
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            node = node.rchild

    def middle_tarverse_by_stack(self, root):
        if not root:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            print node.elem
            node = node.rchild

    def later_traverse_by_stack(self, root):
        if not root:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:
            print myStack2.pop().elem

    def level_tarverse(self, root):
        if not root:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print node.elem
            if node.lchild:
                myQueue.append(node.lchild)
            if node.rchild:
                myQueue.append(node.rchild)
