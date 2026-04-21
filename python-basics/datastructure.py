# append
# - Ordered, mutable, and can hold mixed data types.

my_list = []
my_list.append(2)
my_list.append("hello")
my_list.append(4.44)
my_list.insert(2,9)
print(my_list)

my_list.pop() # remove the last item from list

my_list.pop(0) # remove the first index

print(my_list)

# tuple 
# 	Ordered, immutable, and often used for fixed collections.

my_tuple = (1,2,2,"hello")
print(my_tuple[0])
print(my_tuple[1:3])

# set 
# Unordered, mutable, and stores unique elements.
my_set = {1,2,3,"hello","hello"}
print(my_set)
my_set.add(4)
my_set.remove(2)          # Error if not found
my_set.discard(5) 

# dict 
my_dict = {"name": "Aritra", "score": 95}
my_dict["age"] = 30       # Add new key-value
my_dict["score"] = 100    # Update value
value = my_dict.pop("score")  # Remove and return value
name = my_dict["name"]        # Access value
name = my_dict.get("name")    # Safe access
keys = my_dict.keys()         # All keys
values = my_dict.values()     # All values
items = my_dict.items()       # Key-value pairs
