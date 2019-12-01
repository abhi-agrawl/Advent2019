INPUT = 'input.txt'


def fuel_calulate(mass):

    fuel = mass//3 - 2

    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_calulate(fuel)


def main():

    f = open(INPUT, 'r')

    total_fuel = 0

    for line in f:
        mass = int(line.rstrip('\n'))
        total_fuel += fuel_calulate(mass)

    print(total_fuel)

    f.close()


#######################################################
if __name__ == '__main__':
    main()
