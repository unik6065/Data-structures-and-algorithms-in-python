from LinkedList import LinkedList
from Link import Link
def identity(x): return x           # Identity function

class DoubleEndedList(LinkedList):      # A linked list with access to both ends of the list
    def __init__(self):
        self.__first = None             # Reference to first Link, if any
        self.__last = None              # Reference to last link, if any

    def getFirst(self): return self.__first # Return the first link

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
            if (link is None or self.getLast() is None):
                self.__last = link
        else:
            raise Exception('First link must be Link or None')

    def getLast(self): return self.__last

    def last(self):
        if self.isEmpty():
            raise Exception('No last element in empty list')
        return self.__last.getData()

    def insertLast(self, datum):
        if self.isEmpty():
            return self.insert(datum)
        link = Link(datum, None)
        self.__last.setNext(link)
        self.__last = link

    def insertAfter(self, goal, newDatum, key=identity):
        link = self.find(goal, key)
        if link is None:
            return False
        newLink = Link(newDatum, link.getNext())
        link.setNext(newLink)
        if link is self.__last:
            self.__last = newLink
        return True

    def delete(self, goal, key=identity):
        if self.isEmpty():
            raise Exception('Cannot delete from empty linked list')
        previous = self
        while previous.getNext() is not None:
            link = previous.getNext()
            if goal == key(link.getData()):
                if link is self.__last:
                    self.__last = previous
                previous.setNext(link.getNext())
                return link.getData()
            previous = link

        raise Exception('No item with matching key found in list')
