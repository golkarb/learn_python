example="./example.txt"
file=open(example,"r")
print(file.name)
print(file.mode)
Filecontent=file.read()
print(Filecontent)
file.close()
print(file)

print("======================================")
print("file.read()")
with open("./example.txt", "r") as file2:
    Filecontent=file2.read()
    Filecontent=Filecontent.split("\n")
    for line in Filecontent:
        print(line)

print("======================================")
print("line in file")
with open("./example.txt", "r") as file3:
    for line in file3:
        print(line)

print("======================================")
print("file.readlines()")
with open("./example.txt", "r") as file3:
    fileaslist=file3.readlines()

for line in fileaslist:
    print(line)

print("======================================")
print("file.write()")
with open("./example.txt","r") as file1:
    with open("./example2.txt","w") as file2:
        for line in file1:
            file2.write(line)
with open("./example2.txt","r") as file3:
    for line in file3:
            print(line)

print("======================================")
print("Write CSV file example")
student_list = [{"Student ID": 1, "Gender": "F", "Name": "Emma"},
       {"Student ID": 2, "Gender": "M", "Name": "John"},
       {"Student ID": 3, "Gender": "F", "Name": "Linda"}]

# Write csv file
with open('Example_csv.csv','w') as writefile:
    # Set header for each column
    for col_header in list(student_list[0].keys()):
        writefile.write(str(col_header) + ", ")
    writefile.write("\n")

    # Set value for each column
    for student in student_list:
        for col_ele in list(student.values()):
            writefile.write(str(col_ele) + ", ")
        writefile.write("\n")

# Print out the result csv
with open('Example_csv.csv','r') as testwritefile:
    print(testwritefile.read())
