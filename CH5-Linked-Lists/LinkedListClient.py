from LinkedList import LinkedList

llist = LinkedList()
for item in [0,1,4,9,16]:
    llist.insert(item)

it = llist.iterator()
print('Created an iterator', it)

try:
    while True:
        print('The next item is', it.next())
except StopIteration:
    print('End of iterator')

ite = llist.iterator()
print('Created an iterator', ite)

while ite.hasMore():
    print('The next item is:', ite.next())

print('End of iterator')
