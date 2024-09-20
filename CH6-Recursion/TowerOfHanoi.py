from SimpleStack import Stack

class TowerOfHanoi(object):     # Model the Tower on 3 spindles using 3 stacks
    def __init__(self, nDisks=3):
        self.__stacks = [None] * 3
        self.__labels = ["L", "M", "R"]
        self.__nDisks = nDisks
        self.reset()

    def reset(self):
        for spindle in range(3):
            self.__stacks[spindle] = Stack(self.__nDisks)
            if spindle == 0:
                for disk in range(self.__nDisks, 0, -1):
                    self.__stacks[spindle].push(disk)

    def label(self, spindle):       # Get the label of spindle
        return self.__labels[spindle]

    def height(self, spindle):
        return len(self.__stacks[spindle])

    def topDisk(self, spindle):
        if not self.__stacks[spindle].isEmpty():
            return self.__stacks[spindle].peek()

    def __str__(self):
        result = ""
        for spindle in range(3):
            if len(result) > 0:
                result += "\n"
            result += (self.label(spindle) + ": " + str(self.__stacks[spindle]))
        return result

    def move(self, source, to, show=False):     # Move a single disk from source spindle to another, possibly printing
        if self.__stacks[source].isEmpty():
            raise Exception('Cannot move from empty spindle' + self.label(source))
        if(not self.__stacks[to].isEmpty() and self.topDisk(source) > self.topDisk(to)):
            raise Exception('Cannot move disk' + str(self.topDisk(source)) + 'on top of disk ' + str(self.topDisk(to)))
        self.__stacks[to].push(self.__stacks[source].pop())
        if show:
            print('Move disk', self.topDisk(to), 'from spindle', self.label(source), 'to', self.label(to))

    def solve(self, nDisks=None, start=0, goal=2, spare=1, show=False):         # Solve the puzzle to move
        if nDisks is None:
            nDisks = self.height(start)
        if nDisks <= 0:
            return
        if self.height(start) < nDisks:
            raise Exception('Not enough disks(', str(nDisks), ') on starting spindle', self.label(start))
        self.solve(nDisks - 1, start, spare, goal, show)
        self.move(start, goal, show)
        if show: print(self)
        self.solve(nDisks - 1, spare, goal, start, show)
        if (nDisks == self.__nDisks and show):
            print('Puzzle complete')
