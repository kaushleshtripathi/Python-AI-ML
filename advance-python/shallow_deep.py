import copy

list1 = [[1,2,3],[4,5,6]]

list2 = copy.copy(list1)  # this will create a shallow copy 

list2[0][0] = 9

print(list1)  # list1 item will be change
print(list2)  # list2 item will be change 

print(id(list1))  # id will be different
print(id(list2))  # id will be different 

# -----------------------------------------------------------------------------------------



list1 = [[1,2,3],[4,5,6]]

list2 = copy.deepcopy(list1)  # this will create a deep copy 

list2[0][0] = 9

print(list1)  # list1 items will be same
print(list2)  # list2 item will be change 

print(id(list1))  # id will be different
print(id(list2))  # id will be different     