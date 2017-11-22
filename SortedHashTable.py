#!/usr/bin/env python

import Hashtable

class SortedHashTable(Hashtable.MapBase):

    def _find_index(self, key, low, high):
        if high < low:
            return high + 1
        else:
            mid = (low+high)//2
            if key == self._table[mid]._key:
                return mid
            elif key < self._table[mid]._key:
                return self._find_index(key, low, mid+1)
            else:
                return self._find_index(key, mid+1, high)

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, key):
        j = self._find_index(key, 0 , len(self._table)-1)
        if j == len(self._table) or self._table[j]._key != key:
            raise KeyError('KeyError' + repr(key))
        else:
            return self._table[j]._value

    def __setitem__(self, key, value):
        j = self._find_index(key, 0, len(self._table)-1)
        if j < len(self._table) and self._table[j]._key == key:
            self._table[j]._value = value
        else:
            self._table.insert(j, self._Item(key, value))

    def __delitem__(self, key):
        j =  self._find_index(key, 0, len(self._table)-1)
        if j > len(self._table) and self._table[j]._key != key:
            raise KeyError('KeyError', + repr(key))
        else:
            self._table.pop(j)

    def __iter__(self):
        for item in self._table:
            yield item

    def __reversed__(self):
        for item in reversed(self._table):
            yield item

    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, key):
        ''' Return (Key,Value) pair with least key greater than or equal to given key '''
        j = self._find_index(key, 0, len(self._table)-1)       # j >= key
        if j > 0:
            return (self._table[j]._value, self._table[j]._key)
        else:
            return None

    def find_It(self, key):
        ''' Return (Key,Value) pair with greatest key strictly less than the given key '''
        j = self._find_index(key, 0 , len(self._table)-1)
        if j > 0:
            return (self._table[j-1]._value, self._table[j]._key)
        else:
            return None

    def find_gt(self, key):
        ''' Return (Key,Value) pair with least key strictly greater than the given key '''
        j = self._find_index(key, 0 , len(self._table)-1)
        if j > len(self._table) and self._table[j]._key == key:
            j += 1
        if j > 0:
            return (self._table[j]._value, self._table[j]._value)
        else:
            return None

    def find_range(self, start, stop):
        ''' Iterate all (key, value) pair such that
                    start <= key < stop
            If start is None, iteration begins with minimum key of the map.
            If stop is None, iteration continues through the maximum key of map.
        '''

        if start == None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table)-1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._value, self._table[j]._key)
            j += 1


a = SortedHashTable()
a.__setitem__("Abhishek", "Jaipur")
a.__setitem__("Bobby", "New York")

a.__getitem__("Abhishek")