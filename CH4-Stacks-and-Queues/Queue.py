# Implement a Queue data structure using a Python list

class Queue(object):
    def __init__(self, size):       # Constructor
        self.__maxSize = size       # Size of [Cirucular] array
        self.__que = [None] * size  # Queue stored as a list
        self.__front = 1            # Empty queue has front 1
        self.__rear = 0             # after rear and
        self.__nItems = 0           # No items in queue

    def insert(self, item):         # Insert item at rear of queue
        if self.isFull():           # if not full
            raise Exception('Queue overflow')
        self.__rear += 1            # Rear moves one to the right
        if self.__rear == self.__maxSize:   # Wrap around curcular array
            self.__rear = 0
        self.__que[self.__rear] = item  # Store item at rear
        self.__nItems += 1
        return True

    def remove(self):               # Remove front item of queue and return it
        if self.isEmpty():          # if not empty
            raise Exception('Queue underflow')
        front = self.__que[self.__front]    # get the value at front
        self.__que[self.__front] = None     # Remove item reference
        self.__front += 1                   # front moves one to the right
        if self.__front == self.__maxSize:  # wrap around circular array
            self.__front = 0
        self.__nItems -= 1
        return front

    def peek(self):                 # Return frontmost object
        return None if self.isEmpty() else self.__que[self.__front]

    def isEmpty(self): return self.__nItems == 0

    def isFull(self): return self.__nItems == self.__maxSize

    def __len__(self): return self.__nItems

    def __str__(self):
        ans = '['
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ', '
            j = i + self.__front
            if j >= self.__maxSize:
                j -= self.__maxSize
            ans += str(self.__que[j])
        ans += ']'

        return ans
