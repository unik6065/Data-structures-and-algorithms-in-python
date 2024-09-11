from .Link import Link
from ..LinkedList import LinkedList

def identity(x): return x

class DoublyLinkedList(LinkedList):
    def __init__(self):                         # Constructor
        self.__first, self.__last = None, None

    def getFirst(self): return self.__first
    def getLast(self): return self.__last

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
            if(self.__last is None or link is None):
                self.__last = link
        else:
            raise Exception('First link must be Link or None')

    def setLast(self, link):
        if link is None or isinstance(link, Link):
            self.__last = link
            if(self.__first is None or link is None):
                self.__first = link
        else:
            raise Exception('Last link must be Link or None')

    def traverseBackwards(self, function=print):
        link = self.getLast()
        while link is not None:
            function(link)
            link = link.getPrevious()

    def insertFirst(self, datum):
        link = Link(datum, next=self.getFirst())

        if self.isEmpty():
            self.setLast(link)
        else:
            self.getFirst().setPrevious(link)
            self.setFirst(link)

    insert = insertFirst                # Override parent class insert

    def insertLast(self, datum):
        link = Link(datum, previous=self.getLast())

        if self.isEmpty():
            self.setFirst(link)
        else:
            self.getLast().setNext(link)
            self.setLast(link)

    def deleteFirst(self):
        if self.isEmpty():
            raise Exception('Cannot delete first of empty list')
        first = self.getFirst()
        self.setFirst(first.getNext())
        if self.getFirst():
            self.getFirst().setPrevious(None)
        return first.getData()

    def deleteLast(self):
        if self.isEmpty():
            raise Exception('Cannot delete last of empty list')
        last = self.getLast()
        self.setLast(last.getPrevious())
        if self.getLast():
            self.getLast().setNext(None)
        return last.getData()

    def insertAfter(self, goal, newDatum, key=identity):
        link = self.find(goal, key)
        if link is None:
            return False                # Return failure
        if link.isLast():
            self.insertLast(newDatum)
        else:
            newLink = Link(newDatum, previous=link, next=link.getNext())
            link.getNext().setPrevious(newLink)
            link.setNext(newLink)

        return True

    def delete(self, goal, key=identity):
        link = self.find(goal, key)
        if link is None:
            raise Exception('Cannot find link to delete in list')
        if link.isLast():
            return self.deleteLast()
        elif link.isFirst():
            return self.deleteFirst()
        else:
            link.getNext().setPrevious(link.getPrevious())
            link.getPrevious().setNext(link.getNext())
            return link.getData
