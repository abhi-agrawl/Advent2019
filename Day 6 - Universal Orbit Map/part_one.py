INPUT = "input.txt"
orbit_mapping = {}


def input_data():
    f = open(INPUT, "r")
    orbit_mapping["COM"] = 0

    for line in f:
        object, orbit = line.rstrip("\n").split(")")
        orbit_mapping[orbit] = object
    f.close()


def get_value(object):

    if type(object) == int:
        return object
    else:
        return 1 + get_value(orbit_mapping[object])


def main():

    input_data()
    for orbit in orbit_mapping.keys():
        orbit_mapping[orbit] = get_value(orbit_mapping[orbit])

    ans = sum(orbit_mapping.values())
    print(ans)


#################################################################
if __name__ == "__main__":
    main()
