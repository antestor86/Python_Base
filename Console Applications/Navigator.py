import math
def myDistance(x,y):
    distance = math.sqrt(x**2 + y**2)
    print(distance)
def betweenDistance(x_1,y_1,x_2,y_2):
    distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    print(distance)


choice = int(input('1 - Distance to point; 2 - Distnace between 2 points'))
if choice == 1:
    x = float(input('Set x codinate '))
    y  = float(input('Set y codinate '))
    myDistance(x,y)
elif choice == 2:
    x_1 = float(input('Set x codinate of first point'))
    y_1  = float(input('Set y codinate of first point'))
    x_2 = float(input('Set x codinate of second point'))
    y_2  = float(input('Set y codinate of second point'))
    betweenDistance(x_1,y_1,x_2,y_2)
