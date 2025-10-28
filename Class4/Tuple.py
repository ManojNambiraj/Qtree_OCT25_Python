# Tuple:

mytup = ("apple", "banana", "orange", "grapes")

# print(mytup)
# print(len(mytup))
# print(type(mytup))
# print(mytup[2])

tempList = list(mytup)

print(tempList)
print(type(tempList))

tempList.append("kiwi")
tempList[1] = "bananassss"

mytup = tuple(tempList)

print(mytup)