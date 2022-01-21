# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
from sqlite3 import adapt


fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple (('Apples', 'Oranges', 'Grapes'))

#print (fruits, fruits2)

#fruits2 = ('Mandarinas',)

#print (fruits[2])
#fruits [0]= 'Coco'
print (len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'Apples', 'Oranges', 'Mango'}
#Check if in set***
print ('Apples' in fruits_set)
fruits_set.add ('Coco')
print (fruits_set)
fruits_set.remove ('Coco')
print (fruits_set)
fruits_set.clear()
print (fruits_set)

