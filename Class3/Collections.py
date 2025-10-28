# Collections datatypes:

    # List
    # Tuple
    # Dictionary
    # Set

# List

a = [10, 20, 30, 40, 50]
#     0  1   2   3   4       # Forward indexing
#     -5 -4  -3  -2  -1      # Backward indexing

newList = ["Hello", "Hi"]

print(a)
print(a[1])
print(a[-3])
print(a[0:3])
print(len(a))
print(type(a))

# a[1] = 2000

# a.append(600)
# a.insert(2, 3000)
a.extend(newList)

# a.pop(2)
# a.remove(20)

# a.clear()
# del a

print(a)