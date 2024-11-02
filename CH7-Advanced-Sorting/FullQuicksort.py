import SortArray

def identity(x): return x

class Array(SortArray.Array):
    def __part(self, pivot, lo, hi, key=identity):      # Private function paritions array by items whose keys are below or
        while lo <= hi:
            while(key(self.get(lo)) < pivot):           # Equal a pivot value to the left/low side
                lo += 1
            while(pivot < key(self.get(hi))):
                hi -=1
            if lo >= hi:
                return lo
            self.swap(lo, hi)
            lo, hi = lo + 1, hi -1
        return lo

    def quicksort(self, lo=0, hi=None, short=3, key=identity):
        if hi is None:
            hi = len(self) -1
        short = max(3, short)
        if hi - lo + 1 <= short:
            return self.insert(lo, hi, key)
        pivotItem = self.medianOfThree(lo, hi, key)
        hipart = self.__part(key(pivotItem), lo + 1, hi -1, key)
        self.swap(hipart, hi)
        self.quicksort(lo, hipart -1, short, key)
        self.quicksort(hipart + 1, hi, short, key)

    def medianOfThree(self, lo, hi, key=identity):
        mid = (lo + hi) // 2
        if key(self.get(lo)) > key(self.get(mid)):
            self.swap(lo, mid)
        if key(self.get(lo)) > key(self.get(hi)):
            self.swap(lo, hi)
        if key(self.get(hi)) > key(self.get(mid)):
            self.swap(hi, mid)
        return self.get(hi)

    def insertionSort(self, lo=0, hi=None, key=identity):
        if hi is None:
            hi = len(self) -1
        for outer in range(lo + 1, hi + 1):
            temp = self.get(outer)
            temp_key = key(temp)
            inner = outer
            while(inner > lo and temp_key < key(self.get(inner - 1))):
                self.set(inner, self.get(inner -1))
                inner -= 1
                self.set(inner, temp)
