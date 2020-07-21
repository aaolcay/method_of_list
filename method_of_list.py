"""
------------ SOME METHODS OF LIST -------------
"""
list = [1,2,3,4,5,6,7,8]
for i in dir(list):
    if "__" not in i:
        print(i)
print(25*"==")

###########################################################################################
# For adding something to list we can use append method
list.append(9)
print(list)
############################################################################################

def for_list(list_name):
    for i in list:
        print(i)

print(25*"==")
for_list(list)

#############################################################################################
list.remove(3) # The number 3 is removed by this method in the list has number
# If the number in remove(number) is absent, this code line would be error
print("With remove(3)::{}".format(list))
############################################################################################
# # It takes 2. index of list
list_2 = list.pop(2)
print("With pop(2)::{}".format(list_2))
############################################################################################
# count(x) give number of repetition for x to us
count = list.count(1)
print("count(1) is equal to this number :: {}".format(count))
# For example "1" is repeat once. And count(1) == 1
############################################################################################
# clear() clears everything in a list
list.clear()
print("With clear(), everthing in list was cleared::{}".format(list)) # This code clears everything in the list
############################################################################################
# copy() :::

list_01 = ["Abdullah","Azzam","Olcay",3.14,3.15]
list_02 = []
list_02 = list_01.copy()
print("With copied from list_01 to list_02:",list_02)
############################################################################################
list_01.append("Gebze Technical University")
print(list_01)
# We changed list_01 by appending, but list_02 has not changed
print(list_02)
# If I wrote this code with like this way : list_02 = list_01 , we have been seeing both of them are changing
############################################################################################
# list_1.extend(list_2) ::: list_2 adds to list_1 with this method but list_02 has not changed with this method
list_01.extend(list_02)
print("Extending list_01 is : ",list_01)
print("list_02:",list_02)
############################################################################################
# list_01.index(x) gives index of x in list_01 to us
ind = list_01.index("Gebze Technical University")
print("Index of Gebze Technical University in list_01 is {}".format(ind))
############################################################################################
# list_01.insert(index,elem) elem is added to index number (integer) in list_01
list_01.insert(1,"Sarıyer")
print(list_01)
############################################################################################
# sort() method sorts the elements of a given list in a specific ascending pr descending order
list_01.remove(3.14)
list_01.remove(3.15)
list_01.remove(3.14)
list_01.remove(3.15)
print("Before without sort() method:",list_01)
list_01.sort()
print("After the using sort method of",list_01)
# the list_01 is sorted in alphabetical order
############################################################################################
list_new = [9,1,4,2,8,3]
print("Before without sort() method:",list_new)
list_new.sort()
print("After the using sort method of",list_new)