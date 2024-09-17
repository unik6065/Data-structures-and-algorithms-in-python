from OrderedRecordArray import OrderedRecordArray

arr = OrderedRecordArray(10)

for item in [3, 27, 14, 10, 88, 41, 67, 51, 95]:
    arr.insert(item)

print("Array containing", len(arr), "Items\n", arr)

for goal in [0, 10, 11, 99]:
    print("find(", goal,") returns", arr.find(goal))
