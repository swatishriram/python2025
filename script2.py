names=["sarika","abhi","abhi","chiu","abhi", "aarvi"]
# print(names)
# print(type(names))

# names[0]="shrisha"
# print(names)
# print(len(names))

#del names
#print(names)
# print("sarika" in names)

# for x in range(len(names)):
#     print(names[x])

# i=0
# while (i<len(names)):
#     print(names[i])
#     i=i+1

# insert
names.insert(2,"pooja")
print(names)
# append
names.append("samu")
print(names)
# remove
names.remove("chiu")
print(names)
# sort
names.sort()
print(names)
# clear
# names.clear()
# print(names)
# count()
e=names.count("abhi")
print(e)
#index
e1=names.index("samu")
print(e1)
# pop(1)
names.pop(1)
print(names)
# pop()
names.pop()
print(names)
# reverse()
names.reverse()
print(names)