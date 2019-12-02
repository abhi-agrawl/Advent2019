puzzle_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,
27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,
1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,
2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,
111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,
135,1,135,2,139,1,10,139,0,99,2,0,14,0]

GOAL = 19690720
SIZE = len(puzzle_input)

def part_one(memory):
    for i in range(0, SIZE, 4):

        index_1 = memory[i+1]
        index_2 = memory[i+2]
        index_3 = memory[i+3]

        if memory[i] == 99:
            return memory[0], memory[1], memory[2]

        elif memory[i] == 1:
            addition = memory[index_1] + memory[index_2]
            memory[index_3] = addition

        elif memory[i] == 2:
            product = memory[index_1] * memory[index_2]
            memory[index_3] = product

        else:
            return "Error! Something went wrong."


def part_two():

    for j in range(50, 100):
        for k in range(50, 100):

            memory = puzzle_input[:]
            memory[1] = j
            memory[2] = k

            temp_goal, noun, verb = part_one(memory)

            if GOAL == temp_goal:
                return "{0}{1}".format(noun, verb)

def main():

    memory = puzzle_input[:]
    memory[1] = 12
    memory[2] = 2
    ans1 = part_one(memory)[0]

    ans2 = part_two()

    print("Part One: {0}".format(ans1))
    print("Part Two: {0}".format(ans2))


##################################################################
if __name__ == '__main__':
    main()
