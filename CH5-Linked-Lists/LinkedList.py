from Link import Link
def identity(x): return x           # Identity function


class LinkedList(object):           # A linked list of data elements
    def __init__(self):             # Constructor
        self.__first = None         # Reference to first Link

    def getFirst(self): return self.__first # Return the first Link

    def setFirst(self, link):       # Change the first linkto a new Link
        if link is None or isinstance(link, Link):  # It must be None or a Link object
            self.__first = link
        else:
            raise Exception('First Link must be Link or None')

    def getNext(self): return self.getFirst()       # First link is next

    def setNext(self, link): self.setFirst(link)    # First link is next

    def isEmpty(self):                              # Test for empty list
        return self.getFirst() is None              # True if no first Link

    def first(self):                                # Return the first item in the list
        if self.isEmpty():                          # as long as it is not empty
            raise Exception('No first item in empty list')
        return self.getFirst().getData()            # Return data item (not Link)

    def traverse(self, func=print):                 # Apply a function to all items in list
        link = self.getFirst()                      # Start with first Link
        while link is not None:                     # Keep going until no more links
            func(link.getData())                    # Apply the function to the item
            link = link.getNext()                   # Move on the next Link

    def __len__(self):              # Get length of list
        l = 0
        link = self.getFirst()      # Start with first Link
        while link is not None:     # Keep going until no more links
            l += 1                  # Count links in chain
            link = link.getNext()   # Move on to the next Link
        return l

    def __str__(self):              # Build a string representation
        result = '['                # Enclose list in square brackets
        link = self.getFirst()      # Start with first Link
        while link is not None:     # Keep going until no more links
            if len(result) > 1:     # After first link,
                result += '>'       # separate links with right arrowhead
            result += str(link)     # Append string version of link
            link = link.getNext()   # Move on to the next link
        return result + ']'

    def insert(self, datum):        # Insert a new datum at the start of list
        link = Link(datum,          # Make a new Link fo the datum, what follows is the current list
                    self.getFirst())
        self.setFirst(link)         # Update list to include new Link

    def find(self, goal, key=identity): # Find the first Link whose key matches the goal
        link = self.getFirst()      # Start at the first Link
        while link is not None:
            if key(link.getData()) == goal:         # Does this Link match?
                return link         # If so, return the Link itself
            link = link.getNext()   # Else, continue on along list

    def search(self, goal, key=identity):   # Finds the first item whose key matches goal
        link = self.find(goal, key) # Look for Link obkect that matches
        if link is not None:        # If found,
            return link.getData()   # Return its datum


    def insertAfter(self, goal, newDatum, key=identity):    # Insert a new datum after the first
        link = self.find(goal, key) # Find matching Link object
        if link is None:            # If not found
            return False            # Return failure
        newLink= Link(newDatum, link.getNext()) # Else build a new Link node with new datum and remainder of list
        link.setNext(newLink)       # and insert after matching link
        return True

    def deleteFirst(self):          # Delete first Link
        if self.isEmpty():          # Empty list? raise an exception
            raise Exception('Cannot delete first of empty list')

        first = self.getFirst()     # Stores first Link
        self.setFirst(first.getNext())  # Remove first link from list
        return first.getData()      # Return first Link's data

    def delete(self, goal, key=identity):   # Delete the first Link from the list whose key matches the goal
        if self.isEmpty():          # Empty list? Raise an exception
            raise Exception('Cannot delete from empty linked list')

        previous = self             # Link or LinkedList before Link
        while previous.getNext() is not None:   # to be deleted
            link = previous.getNext()   # Next Link after previous
            if goal == key(link.getData()):     # If next link matches
                previous.setNext(link.getNext())    # Change the previous next to be the Link's next
                return link.getData()           # And return data
            previous = link

        # Since loop ended without finding item, raise exception
        raise Exception('No item with matching key found in list')
