# listA=[11,22,33]
# #retrive
# print(listA[0])

#update
# listA[0]=111
# print(listA)

# #in
# print(111 in listA)

#length
# w=len(listA)
# print(w)

# #delet
# del listA

# #loop
# cities=["sangamner","pune","mumbai","nashik"]
# print(cities)
# for x in range(len(cities)):
#     print(x)
#     print(cities[x])

#for
#for x in cities:
   # print (x)

#while
#i=0
#while(i<=len(cities)):
 #   print(cities[i])
  #  i=i+1
    
#program 3:
#append 
# fruits=["mango","apple","banana","chiku"]
#e=fruits.append("papaya")
#print(e)
#print(fruits)

#reverse
# fruits=["mango","apple","banana","chiku"]
# e1 = fruits.reverse()
# print(e1)
# print(fruits)

# country=["india","pakistan","shrilanka"]
# country1=["USA","england","Aus"]
# e2=country.extend(country1)
# print(e2)
# print(country)

country=["india","pakistan","shrilanka"]
# country.clear()
# print(country)

# country.remove("india")
# print(country)

# country.pop(1)
# print(country)

# country.pop()
# print(country)

# country.insert(3,"Us")
# print(country)

# e=country.count("india")
# print(e)

# e3=country.sort()
# print(e3)
# print(country)

list=[11,22,33,66,44,22,66,55,66,77,88,66]
count= 0
for x in range (len(list)):
    if list[x]== 66:
     count= count + 1
    print(x,list[x])
    
    print(count)