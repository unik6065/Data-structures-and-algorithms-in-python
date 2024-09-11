from LinkedList import LinkedList
from Link import Link
def identity(x): return x               # Identity function


class OrderedList(LinkedList):
    def __init__(self, key=identity):   # An ordered linked list where items are in increasing order by key
        self.__first = None
        self.__key = key

    def getFirst(self): return self.__first

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise Exception('First link must be Link or None')

    def find(self, goal):
        link = self.getFirst()
        while (link is not None and self.__key(link.getData()) < goal):
            link = link.getNext()
        return link                     # Return Link at or just after goal or None for end

    def search(self, goal):
        link = self.find(goal)
        if(link is not None and self.__key(link.getData() == goal)):     # If link found, and its key matches goal
           return link.getData()

    def insert(self, newDatum):             # Insert a new datum based on key order
        goal = self.__key(newDatum)
        previous = self
        while(previous.getNext() is not None and self.__key(previous.getNext().getData()) < goal):
            previous = previous.getNext()
        newLink = Link(newDatum, previous.getNext())
        previous.setNext(newLink)

    def delete(self, goal):                 # Delete first Link with matching key
        if self.isEmpty():
            raise Exception('Cannot delete from empty linked list')
        previous = self

        while(previous.getNext() is not None and self.__key(previous.getNext().getData()) < goal):
            previous = previous.getNext()

        if(previous.getNext() is None or goal != self.__key(previous.getNext().getData())):
            raise Exception('No datum with matching key found in list')

        toDelete = previous.getNext()
        previous.setNext(toDelete.getNext())

        return toDelete.getData()
