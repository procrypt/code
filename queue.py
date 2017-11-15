#!/usr/bin/env python


class Queue:

    def __init__(self):
        self._data = []
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        if self._size == 0:
            return True
        return False

    def first(self):
        if self.is_empty():
            return "Queue Empty."
        return self._data[0]

    def enqueue(self, e):
        self._data.append(e)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue Empty."
        self._size -= 1
        return self._data.pop(0)


a = Queue()

# for i in range(5):
#     a.enqueue(i)
#
# print a.size()
#
# for i in range(a.size()):
#     print a.dequeue()
#
print a.size()

for i in range(a.size()):
    print a.dequeue()