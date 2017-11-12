#!/usr/bin/env python


class Node:
    def __init__(self, element, next):
        self._element = element
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, e):
        if self._head is None:
        self._head = Node(e, self._head)
        if self._head._element > self
        self._size += 1

    def size(self):
        return self._size

    def top(self):
        return self._head._element

    def pop(self):
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

a = LinkedList()
b = [2, 5, 7, 10, 15]