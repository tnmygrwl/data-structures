#!/usr/bin/env python

__author__ = 'kmeelu'


# Implementation of Queue data structure
class Queue(object):
    def __init__(self):
        self.Q = []

    # Enqueue value onto queue
    def enqueue(self, val):
        self.Q.append(val)

    # Dequeue val from queue
    def dequeue(self):
        if self.Q:
            return self.Q.pop(0)
        print('Error: Nothing to dequeue')
        return 'Error'

    # Check if queue empty
    def isEmpty(self):
        return not bool(self.Q)

    # Peek at top queue value
    def peek(self):
        return self.Q[0]

    def __str__(self):
        return str(self.Q)



# Main function includes tests for Queue
def main():
    q = Queue()

    for i in range(10):
        q.enqueue(i)
        print q

    print '\n'

    for _ in range(7):
        print 'Removed %i from the queue' % (q.dequeue())

    print '\nFinal queue:'
    print q


if __name__ == '__main__':
    main()
