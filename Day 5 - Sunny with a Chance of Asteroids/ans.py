INPUT = "input.txt"
data = open(INPUT, "r").read()
int_code = [int(x) for x in data.split(",")]
size = len(int_code)


def parameter_mode(i, n):
    value = n % 10

    if value == 0:
        return int_code[i]
    elif value == 1:
        return i


def values(i, n):
    value1 = int_code[parameter_mode(i+1, n)]
    value2 = int_code[parameter_mode(i+2, n // 10)]

    return value1, value2


def main():

    i = 0
    while i < size:

        opcode = int_code[i] % 100
        n = int_code[i] // 100

        if opcode == 99:
            break

        elif opcode == 1:
            value1, value2 = values(i, n)
            int_code[int_code[i+3]] = value1 + value2

        elif opcode == 2:
            value1, value2 = values(i, n)
            int_code[int_code[i+3]] = value1 * value2

        elif opcode == 3:
            int_code[parameter_mode(i+1, n)] = 5

        elif opcode == 4:
            print(int_code[parameter_mode(i+1, n)])

        elif opcode == 5:
            value1, value2 = values(i, n)
            if  value1 != 0:
                i = value2
            else:
                i += 3

        elif opcode == 6:
            value1, value2 = values(i, n)
            if value1 == 0:
                i = value2
            else:
                i += 3

        elif opcode == 7:
            value1, value2 = values(i, n)
            if value1 < value2:
                int_code[int_code[i+3]] = 1
            else:
                int_code[int_code[i+3]] = 0

        elif opcode == 8:
            value1, value2 = values(i, n)
            if value1 == value2:
                int_code[int_code[i+3]] = 1
            else:
                int_code[int_code[i+3]] = 0

        if opcode in [1, 2, 7, 8]:
            i += 4

        if opcode in [3, 4]:
            i += 2


################################################################

if __name__ == '__main__':
    main()
