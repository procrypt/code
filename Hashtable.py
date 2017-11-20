#!/usr/bin/env  python

from collections import MutableMapping


class MapBase(MutableMapping):

    class _Item:

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self._key == other._key)

        def __cmp__(self, other):
            return self._key < other._key


class UnsortedTableMap(MapBase):

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error' + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        return self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
        raise KeyError('Key Error' + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for items in self._table:
            yield items


a = UnsortedTableMap()
a.__setitem__("Abhishek", "Jaipur")
a.__setitem__("Bobby", "New York")

print a.__getitem__("Abhishek")