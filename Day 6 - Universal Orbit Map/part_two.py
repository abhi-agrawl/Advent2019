INPUT = "input.txt"
orbit_mapping = {}


def input_data():
    f = open(INPUT, "r")
    orbit_mapping["COM"] = 0

    for line in f:
        object, orbit = line.rstrip("\n").split(")")
        orbit_mapping[orbit] = object
    f.close()


def get_distance(final_value, ob):

    if ob == 0:
        return "NOT FOUND"
    elif final_value == ob:
        return "0"
    else:
        return "1" + get_distance(final_value, orbit_mapping[ob])


def main():
    input_data()

    count = 0
    final_value = orbit_mapping["SAN"]

    while True:

        distance = get_distance(final_value, orbit_mapping["YOU"])

        if "NOT FOUND" in distance:
            final_value = orbit_mapping[final_value]
            count += 1
        elif "0" in distance:
            distance = len(distance) - 1 + count
            print(distance)
            break


#################################################################
if __name__ == "__main__":
    main()
