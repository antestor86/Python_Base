rows = 4
columns = 8
row_line = "| " + (columns*"0") + " |"
print(("-"+"-"*columns),end="---\n")
for item in range(rows+1):
    print(row_line,end="\n")
print(("-"+"-"*columns),end="---\n")

