#!/usr/bin/env python


class Node:
    def __init__(self, data, nextNode):
        self._data = data
        self._nextNode = nextNode

    def getData(self):
        return self._data

    def getNext(self):
        return self._nextNode

    def setData(self, newdata):
        self._data = newdata

    def setNext(self, newnext):
        self._nextNode = newnext


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        return self._size

    def add(self, e):
        self._head = Node(e, self._head)
        self._size += 1

    def pop(self):
        if self._size != 0:
            answer = self._head._data
            self._head = self._head._nextNode
            self._size -= 1
            return answer
        print "Stack Empty"
        return 0

    def top(self):
        if self._size != 0:
            return self._head._data
        print "Stack Empty"
        return 0


    def search(self, item):
        current = self._head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            current = current.getNext()
        return found

    def delete(self, data):
        current = self._head
        prev = None
        found = False
        while not found:
            if current._data == data:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:
            self._head = current._nextNode
            self._size -= 1
        else:
            prev.setNext(current.getNext())
            self._size -= 1

    def __iter__(self):
        iter_node = self._head
        while iter_node:
            yield iter_node._data
            iter_node = iter_node._nextNode

a = LinkedList()

a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)

print "-------"
for i in a:
    print i
print "-------"
a.delete(3)
print "-------"
for i in a:
    print i
