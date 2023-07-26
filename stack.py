#!/usr/bin/env python

__author__ = 'kmeelu'


# Implementation of Stack data structure
class Stack(object):
    def __init__(self):
        self.S = []

    # Push value onto stack
    def push(self, val):
        self.S.append(val)

    # Pop value off stack
    def pop(self):
        if self.S:
            return self.S.pop()
        print('Error: Nothing to pop')
        return 'Error'

    # Check if stack empty
    def isEmpty(self):
        return not bool(self.S)

    # Peek at top stack value
    def peek(self):
        if self.S:
            return self.S[-1]
        print('Error: Nothing to peek')
        return 'Error'

    def __str__(self):
        return str(self.S)



# Main function includes tests for Stack
def main():
    s = Stack()

    for i in range(10):
        s.push(i)
        print(s)
    
    print '\n'

    for _ in range(7):
        print "Popped %i from stack!" % (s.pop())

    print("\nFinal stack is:")
    print(s)



if __name__ == '__main__':
    main()
