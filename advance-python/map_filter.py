
import functools

mylist = [1,2,3,4,5,6,7,8,9]

# Step 1: Filter even numbers
print("---",filter(lambda n: n % 2 == 0, mylist))
result_filter = list(filter(lambda n: n % 2 == 0, mylist))  
print(result_filter)

# Step 2: Square (or double) the values
result_map = list(map(lambda n: n * 2, result_filter))      
print(result_map)

# Step 3: Sum all values
result_reduce = functools.reduce(lambda a, b: a + b, result_map)  

print(result_reduce)