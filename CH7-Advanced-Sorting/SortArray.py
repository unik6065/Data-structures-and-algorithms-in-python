class Array(object):
    def __init__(self, initialSize) -> None:    # Constructor
        self.__a = [None] * initialSize         # The array stored as a list
        self.__nItems = 0                       # No items in array initially

    def __len__(self):                          # Special def for len() func
        return self.__nItems                    # Return number of items

    def get(self, n):                           # Return the value at index n
        if 0 <= n and n < self.__nItems:        # Check if n is in bounds, and
            return self.__a[n]                  # ony return item if in bounds

    def set(self, n, value):                    # Set the value at index n
        if 0 <= n and n < self.__nItems:        # Check if n is in bounds, and
            self.__a[n] = value                 # only set item if in bounds

    def swap(self, j, k):                       # Swap the values at 2 indices
        if (0 <= j and j < self.__nItems and    # Check if indices are in bounds
            0 <= k and k < self.__nItems):      # before processing
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):                     # Insert item at the end
        if self.__nItems >= len(self.__a):      # If array is full
            raise Exception('Array overflow')   # Raise exception
        self.__a[self.__nItems] = item          # Item goes at current end
        self.__nItems += 1                      # Increment number of items

    def find(self, item):                       # Find index for item
        for j in range(self.__nItems):          # Among current items
            if self.__a[j] == item:             # If found
                return j                        # then return index to item
        return -1                               # Not found -> return -1

    def search(self, item):                     # Search for item
        return self.get(self.find(item))        # and return item if found

    def delete(self, item):                     # Delete the first occurence
        for j in range(self.__nItems):          # of an item
            if self.__a[j]== item:              # Found item
                self.__nItems -= 1              # One fewer at end
                for k in range(j, self.__nItems):   # Move items from
                    self.__a[k] = self.__a[k + 1]   # right over 1
                return True                     # Return success flag
        return False                            # Made it here, so couldn't find the item


    def traverse(self, function=print):         # Traverse all items
        for j in range(self.__nItems):          # and apply a function
            function(self.__a[j])

    def __str__(self):                          # Special def for str() function
        ans = "["                               # Surround with square bracket
        for i in range(self.__nItems):          # Loop through items
            if len(ans) > 1:                    # Except next to left bracket,
                ans += ", "                     # Separate items with comma
            ans += str(self.__a[i])             # Add string form of item
        ans += "]"                              # Surround with square bracket
        return ans

    def median(self):                           # Calculate the median and return it
        self.insertionSort()                    # First sort the array
        return self.__a[self.__nItems // 2]     # Return the value in the middle

    ## Sorting methods ##

    def bubbleSort(self):                       # Sort comparing adjacent vals
        for last in range(self.__nItems-1, 0, -1):  # and bubble up
            for inner in range(last):           # Inner goes up to last
                if self.__a[inner] > self.__a[inner + 1]: # If elem less than
                    self.swap(inner, inner + 1) # than adjacent value, swap


    def selectionSort(self):                    # Sort by repeated inserts
        for outer in range(self.__nItems-1):    # Swapping in to the leftmost
            min = outer                         # Assume min is leftmost
            for inner in range(outer + 1, self.__nItems):   # Hunt to the right
                if self.__a[inner] < self.__a[min]:     # If we find a smaller number
                    min = inner                 # Update min index
            self.swap(outer, min)               # Swap leftmost and min

    def insertionSort(self):                    # Sort by repeated inserts
        for outer in range(1, self.__nItems):   # Mark one element
            temp = self.__a[outer]              # Store marked elem in temp
            inner = outer                       # Inner loop start at mark
            while inner > 0 and temp < self.__a[inner -1 ]:     # If marked
                self.__a[inner] = self.__a[inner -1]    # elem smaller, then
                inner -= 1                      # shift elem to right
            self.__a[inner] = temp              # Move marked elem to 'hole'
