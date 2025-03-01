numbers1=[11,22,33]
print(numbers1)
print(type(numbers1))

numbers=(111,22,33)
print(numbers)
print(type(numbers))

# e=numbers1[0]=44
# print(e)
# print(numbers1)

# e1=numbers[0]=11
# print(e1)
# print(numbers)

#value stored by Index
# numbers[0]=111
# numbers1[1]=11

#mutable or immutable
fruits=["apple","papaya","banana","mamgo"]
fruits1=("apple","papaya","banana","mamgo")
fruits[0]="chiku"
print(fruits)
#fruits1[1]="grapes"

#particular element present or not
print("chiku" in fruits)
print("apple" in fruits1)

# len
print(len(fruits1))
print(len(fruits))

#loop
marks=[100, 80,90,75,55]
marksA=(50,60,45,77,99)
print(marks)
print(marksA)

# #for loop with range
# for x in range (len(marks)):
#     print(marks[x])

# for y in range(len(marksA)):
#     print(marksA[y])

for x in marksA:
    print(x)

for x in marks:
    print(x)

#while
i=0
while(i<len(marks)):
    print(marks[i])
    i=i+1

a=10,
b=10,20
c=(10,20,30)
print(type(a))
print(type(b))
print(type(c))

city="ahilyanagar"
#slicing(startindex:endindex(not included):steps)

print(city[:10])
print(city[::-1])
print(city[-2:8:2])