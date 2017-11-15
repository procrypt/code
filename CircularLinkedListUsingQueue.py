#!/usr/bin/env python


class Node:
    def __init__(self, data, nextNode):
        self._data = data
        self._nextNode = nextNode

class CircularQueue:
    def __init__(self):
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        if self._size == 0:
            return True
        return False

    def first(self):
        if self.is_empty():
            return "Queue Empty"
        element = self._tail._nextNode
        return element._data

    def enqueue(self, e):
        node = Node(e, self._tail._nextNode)
        if self._size == 1:
            self._tail = node
        else:
            node._nextNode = self._tail._nextNode
            self._tail._nextNode = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue Empty"
        element = self._tail._nextNode
        if self._size == 1:
            self._tail = None
        else:
            self._tail._nextNode = head._nextNode
        return head._data

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._nextNode