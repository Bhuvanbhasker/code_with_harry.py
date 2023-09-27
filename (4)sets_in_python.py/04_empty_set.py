a = {}#Impotant: this syntax will create an empty dictionary and not an empty set.
print(type(a))
#An empty set can be created using the below syntax:
b = set()
print (type(b))

# Adding value to an empty set
#list sign is not use in set
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add(5)# adding a value repeatedly does changes a set
b.add((4, 5, 6))
print(b)

#propeties of sets
#sets are unordered
#there is no way to change items in sets
#sets cannot contain duplicate values 

#length of the set
print(len(b))#print the length of this set

#removal an item
b.remove(5)#remove 5 from the set b
b.remove(15)#throws an error while trying to remove 15
print(b)

print(b.pop())


