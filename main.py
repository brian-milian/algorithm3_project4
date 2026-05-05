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
    identifications = list(map(int, data.split()))

    # my algorithm

    # my hash function
    def my_hash_function(key, table_size):
        return key % table_size
    
    # from here you can update the size of the table
    table_size = 30
    table = [[] for _ in range(table_size)]
    ##keeping_track_of_order = []

    # pseudocode:
    # my pseudocode has changed a couple of times

    for element in identifications:

        hash_index = my_hash_function(element, table_size)

        # if element is not at hash_index
        if not table[hash_index]:
            table[hash_index] = [element, 1]
            ##keeping_track_of_order.append([element, 1])

        # if element does NOT equal element at hash_index
        #         [   row    ][index at row][key]
        elif table[hash_index][       0    ][ 0 ] != element:
            found = False
            # look for element in row
            for item in table[hash_index]:
                if item[0] == element:
                    item[1] += 1
                    found = True
            # if element not found in row, add it to the end of row
            if found == False:
                table[hash_index][0].append([element, 1])
                ##keeping_track_of_order.append([element, 1])
        
        # if element DOES EQUAL element at hash_index, increment value by 1
        else:
            #    [   row    ][index at row][value]
            table[hash_index][      0     ][  1  ] += 1


    # now we just have to loop through table and print output as mentioned in document
    # print duplicates and appearances
    # print total unique IDs
    # print total duplicate IDs

    # for row in table:
    #     for bucket in row:
    #         if bucket[1] > 1:
    #             keeping_track_of_order.append([bucket[0], bucket[1]])
    
    # we basically loop through IDs a second time to print duplicates with their occurences (in order of first appearance)
    write_output_file("output.txt", "Duplicates found (in order of first appearance): ")
    for element in identifications:
        hash_index = my_hash_function(element, table_size)
        # we look for element in row if not in the first index
        #         [   row    ][index at row][key]
        if table[hash_index][       0    ][ 0 ] != element:
            # look for element in row
            for item in table[hash_index]:
                if item[0] == element and item[1] > 1:
                    write_output_file("output.txt", element, " -> appears ", item[1], " times")
        # we print element only if it is a duplicate 
        #         [   row    ][index at row][key]
        if table[hash_index][       0    ][ 0 ] == element and table[hash_index][       0    ][ 1 ] > 1:
            write_output_file("output.txt", element, " -> appears ", item[1], " times")

  

    
    


if __name__ == "__main__":
    main()