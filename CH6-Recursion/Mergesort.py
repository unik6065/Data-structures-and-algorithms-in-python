def identity(x): return x

from Array import Array

class Mergesort(object):        # An object to mergesort Arrays
    def __init__(self, unordered, key=identity):
        self.__arr = unordered
        self.__key = key
        n = len(unordered)
        self.__work = Array(n)
        for i in range(n):
            self.__work.insert(None)
        self.mergesort(0, n)

    def mergesort(self, lo, hi):
        if lo + 1 >= hi:
            return
        mid = (lo + hi) // 2
        self.mergesort(lo, mid)
        self.mergesort(mid, hi)
        self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):
        n = 0
        idxLo = lo
        idxHi = mid
        while(idxLo < mid and idxHi < hi):
            itemLo = self.__arr.get(idxLo)
            itemHi = self.__arr.get(idxHi)
            if (self.__key(itemLo <= self.__key(itemHi))):
                self.__work.set(n, itemLo)
                idxLo += 1
            else:
                self.__work.set(n, itemHi)
                idxHi += 1
            n += 1
        while idxLo < mid:
            self.__work.set(n, self.__arr.get(idxLo))
            idxLo += 1
            n += 1

        while n > 0:
            n -= 1
            self.__arr.set(lo + n, self.__work.get(n))
