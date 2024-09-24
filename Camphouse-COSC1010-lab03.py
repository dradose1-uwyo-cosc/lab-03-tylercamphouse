# Tyler Camphouse
# UWYO COSC 1010
# 9/23/24
# Lab 03 
# Lab Section: 16

# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
print("The list of states contains Wyoming, Colorado, and Montana in that order.")

list = ["Wyoming","Colorado","Montana"]

#now print list
print(list)

#now print the first element in the list
print(list[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(list[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{list[1].upper()} is south of {list[0].upper()}")

print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
other = ["Washington", "Oregon", "California"]
list = list + other
print(list)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
list[4] = "Maine"
print(list)
#Insert the state Texas to be the third element in the list, again printing your list
list.insert(2,"Texas")
print(list)
#Using the `del` statement remove the fourth item from the list, print your list 
del list[3]
print(list)

#Remove Texas using its value, print the list
list.remove("Texas")
print(list)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 

print(f"Sorted: {sorted(list)}")
print(f"Unsorted: {list}")

#Permanently sort your list in reverse order, printing it out
list.reverse()
print(list)

#Using the reverse method reverse the list and print it
list.reverse()
print(list)