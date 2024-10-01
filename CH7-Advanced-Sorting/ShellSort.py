import SortArray

class Array(SortArray.Array):

    def Shellsort(self):
        h = 1
        while 3 * h + 1 < len(self):
            h = 3 * h + 1
        nShifts = 0
        while h > 0:
            for outer in range(h, len(self)):
                temp = self.get(outer)
                inner = outer
                while inner >= h and temp < self.get(inner - h):
                    self.set(inner, self.get(inner - h))
                    inner -= h
                    nShifts += 1
                    if inner < outer:
                        self.set(inner, temp)
                        nShifts += 1
            h = (h - 1) // 3
        return nShifts
