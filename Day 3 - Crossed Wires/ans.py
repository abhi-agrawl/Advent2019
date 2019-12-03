f = open('input.txt','r')
wires = [wire for wire in f]
WIRE1 = [value for value in wires[0].rstrip('\n').split(',')]
WIRE2 = [value for value in wires[1].rstrip('\n').split(',')]
f.close()

def get_coordinates(wire):
    global count
    x = 0
    y = 0
    length = 0
    coordinates = {}

    for value in wire:
        direction = value[0]
        steps = int(value[1:])

        for i in range(steps):

            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -=1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1

            length += 1

            if (x, y) not in coordinates:
                coordinates[(x, y)] = length

    return coordinates


wire1_coordinates = get_coordinates(WIRE1)
wire2_coordinates = get_coordinates(WIRE2)

same_coordinates = list( set(wire1_coordinates.keys()).intersection( set(wire2_coordinates.keys())  ) )

min_origin = min([abs(x) + abs(y) for x, y in same_coordinates])
min_length = min([ wire1_coordinates[value] + wire2_coordinates[value] for value in same_coordinates])

print(min_origin)
print(min_length)
