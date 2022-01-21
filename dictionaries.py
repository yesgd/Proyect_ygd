# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

from unicodedata import name


person = {
    'first_name': 'Yesenia',
    'last_name': 'Garcia',
    'age' : 36
}

print (person ['first_name'])
print (person.get ('last_name'))

# Add key/value
person ['phone'] = '609418736' 
print (person)

#Get dict keys
print (person.keys())
#Get dict items
print ( person.items ())

#Copy dict

person2 = person.copy()
person2 ['city'] = 'New York'
print (person2)

#Remove item
del(person['age'])
print (person)
person.pop ('phone')
print (person)

#Clear
person.clear()
print (person)

#Get length
print (person2)
print (len(person2))

#List of dict
people = [
    {'name' : 'Martha', 'age': 30},
    {'name' : 'Kevin', 'age': 25}
]

print(people)
print(people[1]['name'])

