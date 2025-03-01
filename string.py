fn="shriram"
print(fn)
print(type(fn))

fn='swati'
print(fn)
print(type(fn))

info="""
i am learning java and python
for automation testing this is very imp languase
"""
print(info)

info1='''
i am learning java and python
for automation testing this is very imp languase
'''
print(info1)

city="pune"
print(city)
g=print(len(city))
print(g)

g=city[0]
print(g)

#mutable
city1="mumbai"
#city1[0]='y'
print(city1[0])
print("m" in city1)
print("mu" in city1)
print("bai" in city1)

city="pune"
print(city)

#loop
# for c in range(len(city)):
#     print(c)
#     print(city[c])

for x in city:
    print(x)

i=0
while(i<len(city)):
    print(city[i])
    i=i+1


city="chandrapur"

#slicing:(startindex:endindex(not included):step)
print(city[:6])
print(city[1:4])
print(city[0:10])
print(city[2:-1])
print(city[::2])
print(city[::-1])   #reverse way print string


#my firstname is shriram and lastname is kanwade
fn="shriram"
ln="kanawade"

print("my firstname is "+fn+ " and lastname is "+ln)