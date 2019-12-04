INPUT = "245318-765747"

def part_one():
    initail_value, final_value = [int(i) for i in INPUT.split('-')]

    count = 0
    possible_pass = []

    for value in range(initail_value, final_value+1):
        adjacent_check = False
        increase_check = True
        value = str(value)

        for i in range(1, len(value)):

            if value[i-1] == value[i]:
                adjacent_check = True

            if value[i] < value[i-1]:
                increase_check = False

        if adjacent_check and increase_check:
            possible_pass.append(value)
            count += 1

    print(count)
    return possible_pass


def part_two(possible_pass):
    count = 0

    for value in possible_pass:

        count_dict = {}

        for i in range(1, len(value)):

            if value[i-1] == value[i]:
                if value[i] not in count_dict.keys():
                    count_dict[value[i]] = 1
                else:
                    count_dict[value[i]] += 1

        if 1 in [int(x) for x in count_dict.values()]:
            count += 1

    print(count)


def main():

    possible_pass = part_one()
    part_two(possible_pass)



##################################################################
if __name__ == '__main__':
    main()
