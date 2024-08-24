def identity(x): return x               # Identity function

class PriorityQueue(object):
    def __init__(self, size, pri=identity):  # constructor
        self.__maxSize = size           # Size of array
        self.__que = [None] * size      # Queue stored as a list
        self.__pri = pri                # Func to get item priority
        self.__nItems = 0               # no items in queue

    def insert(self, item):             # Insert items at the rear
        if self.isFull():               # if not full
            raise Exception('Queue overflow')
        j = self.__nItems -1            # Start at front
        while j >= 0 and (self.__pri(item) >= self.__pri(self.__que[j])):   # Look for place by priority
            self.__que[j+1] = self.__que[j] # Shift items to front
            j -= 1
        self.__que[j + 1] = item        # Step towards rear
        self.__nItems += 1              # Insert nre item at rear
        return True

    def remove(self):                   # Return front item of priority
        if self.isEmpty():              # queue, if not empty, & remove
            raise Exception('Queue underflow')

        self.__nItems -= 1              # One fewer item in queue
        front = self.__que[self.__nItems]   # Store te frontmost item
        self.__que[self.__nItems] = None    # Remove item reference
        return front

    def peek(self):
        return None if self.isEmpty() else self.__que[self.__nItems]

    def isEmpty(self): return self.__nItems == 0

    def isFull(self): return self.__nItems == self.__maxSize

    def __len__(self): return self.__nItems

    def __str__(self):
        ans = '['
        for i in range(self.__nItems -1, -1, -1):
            if len(ans) > 1:
                ans += ', '
            ans += str(self.__que[i])

        ans += ']'
        return ans
