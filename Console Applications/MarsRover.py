room_width = 15
room_height = 20
start_position_x = 8
start_position_y = 10
while True:
    print("[PROGRAMM]: Mars Rover is in position  ",start_position_x,start_position_y)
    operator_command = input("[OPERATOR]: ")
    if operator_command == "W":
        if start_position_y == 20:
            continue
        start_position_y += 1
    elif operator_command == "S":
        if start_position_y == 0:
            continue
        start_position_y -= 1
    elif operator_command == "A":
        if start_position_x == 0:
            continue
        start_position_x -= 1
    elif operator_command == "D":
        if start_position_x == 15:
            continue
        start_position_x += 1
    # elif start_position_x == 0 and start_position_x > 15 and start_position_y == 0 and start_position_y > 20:
    #      continue
    else:
        print("Write Correct Word")
        break

