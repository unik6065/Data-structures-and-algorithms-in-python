import BadArray
maxSize = 10
arr = BadArray.Array(maxSize)

arr.insert(77)
arr.insert(99)
arr.insert('foo')
arr.insert('bar')
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert('baz')
arr.insert(-17)

print("Array containing", arr.nItems, "items")

arr.traverse()

print('search for 12 returns', arr.search(12))
print('search for 12.34 returns', arr.search(12.34))
print('deleting 0 return', arr.delete(0))
print('deleting 17 return', arr.delete(17))

print("Array after deletions has", arr.nItems, "items")
arr.traverse()
