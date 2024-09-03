from DoubleEndedList import DoubleEndedList

def second(x): return x[1]

dList = DoubleEndedList()

print('Initial list has ', len(dList), ' element(s) and empty = ', dList.isEmpty())

after = None
people = ['Raj', 'Amir', 'Adi', 'Don', 'Ken', 'Ivan']

for i, person in enumerate(people):
    if after:
        dList.insertAfter(after, (i * i, person), key=second)
    else:
        dList.insert((i*i, person))

print('After inserting, ', len(dList) -1, ' persons into the linked list after ', after, ' it contains: ')
dList.traverse()
print ('First: ', dList.first())

next = (404, 'Tim')
dList.insertLast(next)
print('After inserting, ', next, ' at the end, the double linked list contains:\n', dList)

dList.insert(next)
print('After inserting, ', next, ' at the front, the double linked list contains:\n', dList)
print('Deleting the first item returns, ',dList.deleteFirst(), ' and leaves the double linked list containing:\n', dList,
      'with first: ', dList.first(), 'and last: ', dList.last())

print('Deleting the last item returns, ', dList.delete(second(dList.last()), key=second), ' and leaves the double linked list containing:\n', dList,
      'with first: ', dList.first(), 'and last: ', dList.last())

print('Removing some items from the linked list by key: ')

for person in people[0:5:2]:
    dList.delete(person, key=second)
    print('After deleting ', person, 'the list is ', dList)
    if not dList.isEmpty():
        print('The last item is ', dList.last())

print('Removing remaining items from the front of the linked list: ')

while not dList.isEmpty():
    print('After deleting; ', dList.deleteFirst(), 'the list is', dList)
    if not dList.isEmpty:
        print('The last item is', dList.last())
