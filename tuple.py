# a=10,
# print(a)
# print(type(a))

# b=10,2
# print(b)
# print(type(b))

# c=(11,22,33,44,55)
# print(c)

# #does tuple stores value by index----> yes
# d=(11,12,13,14,15)
# print(d[0])

# #mutable or not
# d1=(11,12,13,14,15)
# d1[0]=101
# print(d1)

#can we store duplicate value inside tuple--->yes
# d3=(11,22,33,11,22,44)
# print(d3) 

#loop
g=(21,22,23,24,25)
print(g)
# print(len(g))
#  #for loop using range

# for x in range(len(g)):
#     print(x)
#     print(g[x])
 
 #while loop using range
i=0
while(i<len(g)):
    print(g[i])
    i=i+1

#particular element available in tuple

print(21 in g)

print(222 in g)

#unpacking tuple
country=("india","pakistan","USA","Australia")
(a,b,c,d)=country
print(a)
print(b)
print(c)
print(d)

country1=("india","pakistan","USA","Australia","india")
e=country1.count("india")
print(e)

e1=country1.index("india")
print(e1)

e2=country1.index("india",2)
print(e2)