myDict = {
    "Pankha":  "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Option are ", myDict.keys())
a = input("Enter the hindi word\n")
#print("the meaning of your word is:", my Dct[a])

#below line will not throw an errror if the key is not present in the dictionary.
print("The meaning of your word is:", myDict[a])