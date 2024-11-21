
def count_letters(text):
    letter = input("Which letter we must find? ")
    number = input("Which number we must find? ")
    letter_count = 0
    number_count = 0
    for word in text:
        if word == letter:
            letter_count += 1
        elif word == number:
            number_count += 1
        else:
           continue
    print("Letters count of letter  ",letter,":",letter_count,end=" ")
    print("Numbers count of number ",number,":",number_count,end="")

text = input("Write text:  ")
count_letters(text)
