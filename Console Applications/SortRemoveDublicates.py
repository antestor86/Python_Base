def mergeLists():
    list1.extend(list2)

def bubble_sort(items):
    for limit in range(len(items) - 1, 0, -1):
        for i in range(limit):
            if items[i] > items[i + 1]:
               items[i], items[i + 1] = items[i + 1], items[i]
    return items

def removeDublicates():
    for item in range(len(list1)-1,0,-1):
        if list1[item] == list1[item - 1]:
            list1.remove(list1[item])
    return list1


list1 = [1, 3, 5, 7, 9]
list2 = [1, 4, 15, 6, 8, 10]
mergeLists()
bubble_sort(list1)
removeDublicates()
print(list1)