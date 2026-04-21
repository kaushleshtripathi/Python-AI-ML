# Filter even numbers
num_list = [0,1,2,3,4,5,6,7,8,9,10]
even_list = []

for num in num_list:
    if num % 2 == 0:
        even_list.append(num)

print(even_list)        


# List comprehension 
# [expression for item in iterable if condition]

evens = [x for x in num_list if x % 2 == 0]
print(evens)
# Output: [0, 2, 4, 6, 8]

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
# Output: [1, 2, 3, 4, 5, 6]


# Dictionary Comprehension 
#{key_expr: value_expr for item in iterable if condition}

grades = {'Alice': 85, 'Bob': 72, 'Charlie': 90}
passed = {name: grade for name, grade in grades.items() if grade >= 80}
# Output: {'Alice': 85, 'Charlie': 90}

