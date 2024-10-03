def identity(x): return x
import SortArray

class Array(SortArray.Array):

    def partition_rec(self, pivot, lo=0, hi= None, key= identity):
        if hi is None:
            hi = len(self) -1
        while (lo <= hi and key(self.get(lo)) < pivot):
            lo += 1
        while (lo < hi and pivot < key(self.get(hi))):
            hi -= 1

        if lo >= hi:
            return lo
        self.swap(lo, hi)
        return self.partition_rec(pivot, lo + 1, hi - 1, key)

    def partition(self, pivot, lo=0, hi=None, key=identity):
        if hi is None:
            hi = len(self) -1
        while lo <= hi:
            while(lo <= hi and key(self.get(lo)) < pivot):
                lo += 1
            while(lo < hi and pivot < key(self.get(hi))):
                hi -= 1
            if lo >= hi:
                return lo
            self.swap(lo, hi)
            lo, hi = lo + 1, hi- 1
        return lo
