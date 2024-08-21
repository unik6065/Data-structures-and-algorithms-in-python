from OrderedRecordArray import OrderedRecordArray

def second(x):
    return x[1]

max_size = 1000
arr = OrderedRecordArray(max_size, second)

# Insert 10 items

for rec in [('a', 3.1), ('b', 7.5), ('c', 6.0), ('d', 3.1),
            ('e', 1.4), ('f', -1.2), ('g', 0.0), ('h', 7.5),
            ('i', 7.5), ('j', 6.0)]:
    arr.insert(rec)

print("Array contening : ",len(arr), " items: \n", arr)

# Deleting a few items, including some duplicates
for rec in [('c', 6.0), ('g', 0.0), ('g', 0.0), ('b', 7.5), ('i', 7.5)]:
    print ("Deleting :", rec, " returns :", arr.delete(rec))

print("Array after deletions has : ", len(arr), " items: \n", arr)

for key in [4.4, 6.0, 7.5]:
    print("find(", key, ") returns ", arr.find(key),
          " and get (", arr.find(key), ") returns", arr.get(arr.find(key)))
