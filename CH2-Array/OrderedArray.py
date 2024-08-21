# Implement an ordered Array data structure

class OrderedArray(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]
        raise IndexError("Index " + str(n) + " is out of range")    # Raise error if n is out of range

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):              # Special def for str() func
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:        # Except next to left bracket,
                ans += ", "         # Separate items with coma
            ans += str(self.__a[i])
        ans += "]"
        return ans

    def find(self, item):       # Find index at or just below
        lo = 0                  # item in ordered list
        hi = self.__nItems -1   # Look between lo and hi

        while lo <= hi:
            mid = (lo + hi) // 2        # Select the midpoint
            if self.__a[mid] == item:   # Did we find item at midpoint?
                return mid              # Return location of item
            elif self.__a[mid] < item:  # Is item in upper half?
                lo = mid + 1            # Yes, raise the lo boundary
            else:
                hi = mid -1             # No, but could be in lowe half

        return lo   # Item not found, return insertion point instead


    def search(self, item):
        index = self.find(item)         # Search for item
        if index < self.__nItems and self.__a[index] == item:
            return self.__a[index]      # and return item if found

    def insert (self, item):                # Insert item into correct position
        if self.__nItems >= len(self.__a) : # If array is full
            raise Exception("Array overflow")  # Raise exceptio

        index = self.find(item) # Find index where item should go
        for j in range(self.__nItems, index, -1): # Move bigger items
            self.__a[j] = self.__a[j - 1]  # To the right

        self.__a[index] = item  # Insert the item
        self.__nItems += 1  # Increment the number of items

    def delete(self, item):                     # Delete any occurrence
        j = self.find(item)                     # Try to find the item
        if j < self.__nItems and self.__a[j] == item : # If found
            self.__nItems -= 1                  # One fewer at end
            for k in range(j, self.__nItems):   # Move bigger elements to left
                self.__a[k] = self.__a[k + 1]
            return True                         # Return success flag

        return False                            # Made it here, item not found
