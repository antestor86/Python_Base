points = []
points_count = int(input("Add points count: "))
for _ in range(points_count):
    point = int(input("Add point: "))
    points.append(point)

minimum = 0
maximum = 0

for item in points:
    if maximum < item:
        maximum = item
    elif minimum < item:
        minimum = item

print(points)
print('The maxmimum value = ',maximum)
print('The minimum value =',minimum)

for i in range(points_count):
    if points[i] == maximum:
        points[i] = minimum
    elif points[i] == minimum:
        points[i] = maximum

print('Replaced points: ',points)
