print("Hello World!")

name = "micheal jackson"
print("before upper:", name, "\nafter upper:", name.upper(),"\n")

print("===================================\n")

tuple1=("disc", 10, (0, 1))
print("example of a tuple (idenitified with round brackets):", tuple1)
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

print("===================================\n")

list1=["Michael", (0, 1), [4, 5]]
print("1st list example (identified with square brackets):", list1)
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
print("list2 does not change as the first element of list4 changes back to 'manzana'':", list2, "\n")

print("===================================\n")

dict1={"key1": 0, "key2": "John", 0: "Mary", "key3": 5}
print("1st dictionary (identified with swiggly brackets):", dict1)
print("keys of the 1st dictionary:", dict1.keys())
del(dict1[0])
print("item with key:0 has been removed:", dict1)

set1={"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print("1st set (identified with swiggly brackets but no keys)", set1)
list5=[1, 2, 3, 4, 5, 5, 1, 2, 3]
print("a list can be converted into a set (but with no duplicates):", set(list5))
set2=set(list5)
set2.add(6)
set2.remove(1)
print("elemets can be added/removed to/from a set:", set2, "\n")

set3={1,2,3,4,5}
set4={3,4,5,6,7}
print("set3:", set3, "set4", set4)
print("union:", set3.union(set4), "difference:", set3.difference(set4), "intersection:", set3.intersection(set4))
