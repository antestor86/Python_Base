#Write a program for a slightly more complicated version of the winning ticket problem.
# There are pre-known ticket numbers: 345, 19, 87, 1020 and 421 (feel free to use your own numbers).
# Now, a ticket is considered a winner if the ticket number is a three-digit number and it is
# divisible by 5. Output to the console a message for each winning ticket and the number of winners.

winners = 0
for ticket in 345,19,87,1020,421,20,535:
    if ticket //1000 == 0 :
        if ticket // 100 != 0 and ticket % 5 == 0:
            print(ticket)
            winners += 1
print("Winners ",winners)