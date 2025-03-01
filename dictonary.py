info=[
    {
        "firstname":"swati",
        "lastname":"bibave",
        "age":28,
        "skills":["python","php","js"],
        "language":"marathi",
        "city":"nashik"
    },
    {
        "firstname":"swara",
        "lastname":"bibave",
        "age":12,
        "skills":["python","php","js"],
        "language":"marathi",
        "city":"pune"
    },
    {
        
        "firstname":"shriram",
        "lastname":"kanwade",
        "age":32,
        "skills":["python","php","js"],
        "language":"hindi",
        "city":"mumbai"
    },
    {
        "firstname":"rutuja",
        "lastname":"kharde",
        "age":28,
        "skills":["python","php","js"],
        "language":"marathi",
        "city":"pune"
    },

]
print(info)
print(type(info))

#total age of person
# total=0
# for person in info:
#     total=total+person["age"]

# print(total/len(info))

#print person firstname with city pune

for person in info:
    if person["city"]=="pune":
     print(person["firstname"])

for person in info:
   person["skills"].append("genAI")

print(info)

#print name nd number of skills
for person in info:
   print(f'{person["firstname"]}:{len(person['skills'])}')

# #list of firstname and lastname
# for person in info:
#    print(person["firstname"])
#    print(person.get("lastname"))