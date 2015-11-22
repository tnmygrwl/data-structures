#!/usr/bin/env python

__author__ = 'kmeelu'


class HashTable(object):
    def __init__(self, buckets=10):
        self.buckets = buckets
        self.T = []
        for _ in range(buckets):
            self.T.append([])

    def hashIt(self, val):
        return hash(val) % self.buckets

    def insert(self, val):
        key = self.hashIt(val)
        self.T[key].append(val)

    def search(self, val):
        key = self.hashIt(val)
        if val in self.T[key]:
            return True
        else:
            return False

    def __str__(self):
        fullStr = 'This Hash Table has format:'
        for i in range(self.buckets):
            fullStr += '\nFor key %i, we get elements: ' % (i)
            fullStr += str(self.T[i])
        return fullStr



def main():
    H = HashTable(4)

    for i in range(0, 99, 3):
        H.insert(i)

    print H

    print H.search(98)
    print H.search(69)


if __name__ == '__main__':
    main()
