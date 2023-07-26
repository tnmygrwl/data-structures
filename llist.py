#!/usr/bin/env python

__author__ = 'kmeelu'


# Class for individual nodes
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getVal(self):
        return self.val

    def getNext(self):
        return self.Next

    def setNext(self, next):
        self.next = next

    def setVal(self, val):
        self.val = val


# Class for linked list as a whole
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def getLength(self):
        return self.length

    def addFirst(self, node):
        self.head = node
        self.tail = node
        self.length += 1

    def addN(self, node):
        if not self.head:
            self.addFirst(node)

        if self.tail:
            self.tail.next = node
        self.tail = node

    def find(self, index):
        start = self.head
        prev = None
        i = 0
        while i < index and start:
            prev = start
            start = start.next
            i += 1
        return prev, start

    def get(self, index):
        (prev, node) = self.find(index)
        return node.val

    def set(self, index, val):
        (prev, node) = self.find(index)
        node.val = val

    def delete(self, index):
        (prev, node) = self.find(index)
        prev.next = node.next if node.next else None

    def __str__(self):
        node = self.head
        i = 0
        list = ''
        while node:
            list += f'{str(i)}: {str(node.val)}' + '\n'
            node = node.next
            i += 1
        return list


def main():
    LL = LinkedList()

    for i in range(10):
        LL.addN(Node(i))

    print(LL)
    LL.set(8,101)
    print LL.get(8)
    LL.delete(8)
    print LL.get(8)


if __name__ == '__main__':
    main()




