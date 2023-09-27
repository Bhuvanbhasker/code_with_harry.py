myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict":{'harry': 'player'},
}
print(myDict['Fast'])
print(myDict['Harry'])
print(myDict['anotherdict']['harry'])
print(list(myDict.keys()))#prints the key of the dictionary.
print(myDict.values())# orints the keys of the dictionary.
print(myDict.items()) #prints the key of the dictionaryprint
print(myDict)
updateDict = {
     "lovish": "freind",
     "divya": "freind",
     "shubham": "freind"
 }
myDict.update(updateDict)
print(myDict)
print(myDict.get("harry"))#print value associated with key "harry"
print(myDict["harry"]) #print value associated with key "harry"

#the difference between .get and [] syntax in dictionaries:
print(myDict.get("harry2")) #return none as harry2 is not present in the dictionary
print(myDict["harry2"] #throw an error as harry is not present in the dictionary
      )
