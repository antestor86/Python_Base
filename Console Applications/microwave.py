reverse_time = int(input("Seconds:"))
seconds = 0
for second in range(reverse_time,-1,-1):
    print(second)
    answer = int(input("Do you want to stop warp up?"))
    seconds += 1
    if answer == 1:
        print("The food is ready, you can pick it up.")
        print(second-1,"second")
        break
    elif answer == 0:
        continue
print("Pick your food, be careful it`s very hot")

