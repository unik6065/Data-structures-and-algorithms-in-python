import LinkedList

class Link(LinkedList.Link):
    def __init__(self, datum, next=None, previous=None):        # One datum in a linked list
        self.__data = datum
        self.__next = next
        self.__previous = previous

    def getData(self): return self.__data
    def getNext(self): return self.__next
    def getPrevious(self): return self.__previous
    def setData(self, datum): self.__data = datum

    def setNext(self, link):
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception('Next link must be Link or None')

    def setPrevious(self, link):
        if link is None or isinstance(link, Link):
            self.__previous = link
        else:
            raise Exception('Previous link must be Link or None')

    def isFirst(self): return self.__previous is None
