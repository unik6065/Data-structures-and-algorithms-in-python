import Array
maxSize = 10
arr = Array.Array(maxSize)

print('Higher value of the array ', arr.deleteMaxNumber())

# arr.insert(77)
# arr.insert(99)
# arr.insert('foo')
# arr.insert('bar')
# arr.insert(44)
# arr.insert(55)
# arr.insert(12.34)
# arr.insert(0)
# arr.insert('baz')
# arr.insert(-17)

arr.insert('foo')
arr.insert('bar')
arr.insert(0)
arr.insert(-1)
arr.insert('baz')

print("Array containing", len(arr), "items")

print('Higher value of the array ', arr.deleteMaxNumber())

arr.traverse()

print('search for 12 returns', arr.search(12))
print('search for 12.34 returns', arr.search(12.34))
print('deleting 0 return', arr.delete(0))
print('deleting 17 return', arr.delete(17))
print('setting item at index 3 to 33')
arr.set(3, 33)

print("Array after deletions has", len(arr), "items")
arr.traverse()
