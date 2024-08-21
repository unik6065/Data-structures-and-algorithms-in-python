from OrderedArray import OrderedArray
max_size = 1000
arr = OrderedArray(max_size)

arr.insert(77)
arr.insert(99)
arr.insert(44)
arr.insert(55)
arr.insert(0)
arr.insert(12)
arr.insert(44)
arr.insert(99)
arr.insert(77)
arr.insert(0)
arr.insert(3)

print("Array contening ", len(arr), "items: ", arr)

arr.delete(0)
arr.delete(99)
arr.delete(0)
arr.delete(0)
arr.delete(3)

print("Array after deletion has ", len(arr), "items: ", arr)

print ("find(44) returns", arr.find(44))
print ("find(46) returns", arr.find(46))
print ("find(77) returns", arr.find(77))
