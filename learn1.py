print("Hello World!")

name = "micheal jackson"
print("before upper:", name, "\nafter upper:", name.upper(),"\n")

tuple1=("disc", 10, (0, 1))
print("example of a tuple:", tuple1)
print("last element of the example tuple is:", tuple1[-1])
print("the first two elements of the tuple are", tuple1[0:2],"\n")

tuple2=(0, ("john", (0,1), "mary"), (1,2,3,4), 5)
print("2nd tuple example:", tuple2)
print("second element of the second element of this tuple is:", tuple2[1][1])
print("all elements of the third element of the this tuple are:", tuple2[2][:])
print("the length of this tuple is:", len(tuple2))
print("the element containing (1,2,3,4) in the tuple is in position:", tuple2.index((1,2,3,4)),"\n")

tuple3=(0, -2, 10)
print("3rd tuple example:", tuple3)
print("sorted tuple generate a list (with square brackets instead of round brackets):", sorted(tuple3),"\n")

list1=["Michael", (0, 1), [4, 5]]
print("1st list example:", list1)
list1.extend(['pop', 23])
print("extending with list ['pop' and 23]:", list1)
list1=["Michael", (0, 1), [4, 5]]
list1.append(['pop', 23])
print("appending with list ['pop' and 23]:", list1,"\n")

string1 = "Michael Jackson is the best"
print("string example:", string1)
print("separate string into a list:", string1.split(), "\n")

string2 = "manzana, banana, pepino"
list2=string2.split(",")
print("a list:", list2," derived from a string:", string2)
list3=list2
print("list3 is created as a reference to the same list:", list3)
list3[0]='naranja'
print("list2 changes as the first element of list3 changes to 'naranja':", list2)
list4=list2[:]
print("list4 is a clone of list2:", list4)
list4[0]='manzana'
print("list2 does not change as the first element of list4 changes back to 'manzana'':", list2)
