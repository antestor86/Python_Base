rows = int(input("Add Rows count: "))
columns = int(input("Add columns count: "))
spaces = int(input("Add spaces betwen rows:"))
for item in range(rows):
    print(("="*columns)+ " " + spaces*"*" + " "+("="*columns),end="\n")
