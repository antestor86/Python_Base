password = input("Write password: ")
numeric_count = 0
correct_password = ""
upper_char_count = 0
if len(password) >= 8:
    for char in password:
       if char.isupper():
          upper_char_count += 1
    if upper_char_count > 0 :
        for i in password:
            if i.isnumeric():
                numeric_count +=1

if numeric_count >= 3 :
    print("The password is correct:")
else:
    print("The password is incorrrect")
