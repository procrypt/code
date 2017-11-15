#!/usr/bin/env python


class Stack:

    def __init__(self):
        self._data = []
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        if self.size() == 0:
            return "Stack Empty"
        return False

    def push(self, e):
        self._data.append(e)
        self._size += 1

    def pop(self):
        return self._data.pop(-1)

    def top(self):
        if self.is_empty():
            return False
        return self._data[-1]


a = Stack()

for i in range(5):
    a.push(i)

print a.size()

for i in range(a.size()):
    print a.pop()
