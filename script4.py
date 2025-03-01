#create
mydict={
    "fname":"swati",
    "lname":"bibave",
    "age":12
}
# print(mydict)
# print(type(mydict))

# print(len(mydict))

# # retrive
# print(mydict)
# e=mydict.get("age")
# print(e)
# # update
# mydict['fname']="samu"
# print(mydict)

# #add
# mydict['language']="marathi"
# print(mydict)

# #search
# print("fname" in mydict)
# # delete
# del mydict["lname"]
# print(mydict)

# #popitem
# mydict.popitem()
# print(mydict)

# mydict.clear()
# print(mydict)

# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

for x in mydict.keys():
    print(x)
for x in mydict.values():
    print(x)
for x in mydict.items():
    print(x)