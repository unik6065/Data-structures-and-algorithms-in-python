# Implement an Ordered Array of Records Structure

def identity(x):       # The identity function
    return x


class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity):  # Constructor
        self.__a = [None] * initialSize             # The array stored as a list
        self.__nItems = 0                           # No items in the array initially
        self.__key = key                            # Key function gets record key

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

    def find(self, key, lo= 0, hi=None):    # Find index at or just below key
        if hi is None:                      # If hi was not provided,
            hi = self.__nItems - 1          # use upper bound of array
        if lo > hi:                         # if range is empty,
            return lo                       # return lo for base case
        mid = (lo + hi) // 2                # Select the midpoint
        if self.__key(self.__a[mid]) == key:    # Did we find it?
            return mid

        if self.__key(self.__a[mid]) < key: # Is it in upper half
            return self.find(key, mid + 1, hi)
        else:
            return self.find(key, lo, mid - 1)

    def search(self, key):
        idx = self.find(key)        # Search for a record by its key
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx]    # And return item if found

    def insert(self, item):                     # Insert item into the correct position
        if self.__nItems >= len(self.__a):      # If array is full,
            raise Exception('Array overflow')   # Raise exception

        j = self.find(self.__key(item))         # Find where item should go

        for k in range(self.__nItems, j, -1) :  # Move biger items right
            self.__a[k] = self.__a[k -1]

        self.__a[j] = item                      # Insert the item
        self.__nItems += 1                      # Increment the number of items

    def delete(self,item):                      # Delete any occurence
        j = self.find(self.__key(item))         # Try to find the item
        if j < self.__nItems and self.__a[j] == item:    # If found
            self.__nItems -1                    # One fewer at end
            for k in range(j, self.__nItems):   # Move bigger items left
                self.__a[k] = self.__a[k+ 1]
            return True                         # Return success flag

        return False        # Made it here, item not found
