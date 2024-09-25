text_palindrom = input("Add text for check:")
counter = 0
palindrom = ""
for item in text_palindrom:
    counter +=1
    palindrom = palindrom +item
    if counter % 2 == 0:
        break
print(palindrom)

