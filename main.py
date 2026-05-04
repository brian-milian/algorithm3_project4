def read_input_file(filename):
    with open(filename, "r") as file:
        data = file.read()
    return data


def write_output_file(filename, output):
    with open(filename, "w") as file:
        file.write(output)


def main():
    # read input
    data = read_input_file("in4c.txt")

    # convert input text to list of ints
    ids = list(map(int, data.split()))

    # my algorithm


    # write to output
    write_output_file("out4c.txt", result)


if __name__ == "__main__":
    main()