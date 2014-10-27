__author__ = 'Ayla'


#1. Create a dictionary of terms. You can use any theme you want: Python keywords, math terms, slang you know, music groups,
#whatever. Put at least five entries in your dictionary.

Horses={'Zim':["Dutch Warmblood/Welsh Pony"], 'Wow': ["Quarter Horse"] ,'Gandalf': ["Irish Sport Horse"],'Foxy': ["Appaloosa" ],'Desi': ["Thoroughbred"]}
breed=[['Zim',"Dutch Warmblood/Welsh Pony"], ['Wow', "Quarter Horse" ],['Gandalf', "Irish Sport Horse"],['Foxy', "Appaloosa"] ,['Desi', "Thoroughbred"]]

#2. Display the value of one of the terms using the [key] method.

print(Horses['Zim'])


#3. Display the value using the .get method.
print(Horses['Zim'])
print(Horses.get('Zim'))


#4. Write a for loop to print out all of the keys in the dictionary.

for name in Horses:
    print(name)
print(Horses)

#print(Horses)


#5. Write a for loop to print out all of the values in the dictionary.

for name in Horses:
    for breed in Horses[name]:
         print(breed)









#6. Write an if statement that prints out 'I like pie' if one of your keys is pie, and prints out 'I want some pie'
#if pie is not one of your keys.

#if Horses:
#    for name in Horse[breed]:
#        print()






#print out values

