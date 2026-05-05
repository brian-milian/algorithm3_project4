import re



def read_input_file(filename):
    with open(filename, "r") as file:
        data = file.read()
    return data


def write_output_file(filename, output):
    with open(filename, "a") as file:
        file.write(output)


def main():
    with open("output.txt", "w") as file:
        pass

    # read input
    data = read_input_file("in4c.txt")

    # convert input text to list of ints
    identifications = list(map(int, re.findall(r"\d+", data)))

    # my algorithm

    # my hash function
    def my_hash_function(key, table_size):
        return key % table_size
    
    # from here you can update the size of the table
    table_size = 30
    table = [[] for _ in range(table_size)]
    total_duplicates = 0
    unique_ids = 0
    ##keeping_track_of_order = []

    # pseudocode:
    # my pseudocode has changed a couple of times

    for element in identifications:

        hash_index = my_hash_function(element, table_size)

        # if element is not at hash_index
        if not table[hash_index]:
            table[hash_index]. append([element, 1])
            ##keeping_track_of_order.append([element, 1])
            unique_ids += 1

        # if element does NOT equal element at hash_index
        #         [   row    ][index at row][key]
        elif table[hash_index][0][0] != element:
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
            unique_ids += 1
        
        # if element DOES EQUAL element at hash_index, increment value by 1
        else:
            #    [   row    ][index at row][value]
            table[hash_index][0][1] += 1
            unique_ids += 1


    # now we just have to loop through table and print output as mentioned in document
    # print duplicates and appearances
    # print total unique IDs
    # print total duplicate IDs

    # for row in table:
    #     for bucket in row:
    #         if bucket[1] > 1:
    #             keeping_track_of_order.append([bucket[0], bucket[1]])
    
    # we basically loop through IDs a second time to print duplicates with their occurences (in order of first appearance)

    keep_track_of_prints = [[] for _ in range(table_size)]
    duplicate_counter = 0

    




    write_output_file("output.txt", "Duplicates found (in order of first appearance): \n")
    for element in identifications:
        hash_index = my_hash_function(element, table_size)
        # we look for element in row if not in the first index
        #         [   row    ][index at row][key]
        if table[hash_index][       0    ][ 0 ] != element:
            # look for element in row
            for item in table[hash_index]:
                if item[0] == element and item[1] > 1 and not keep_track_of_prints[hash_index]:
                    write_output_file("output.txt", f"{element} -> appears {item[1]} times\n")
                    keep_track_of_prints[hash_index].append([element, item[1]])
                    duplicate_counter += 1
                    total_duplicates += item[1]
        # we print element only if it is a duplicate 
        #         [   row    ][index at row][key]
        if table[hash_index][0][0] == element and table[hash_index][0][1] > 1 and not keep_track_of_prints[hash_index]:
            write_output_file("output.txt", f"{element} -> appears {table[hash_index][0][1]} times\n")
            keep_track_of_prints[hash_index].append([element, table[hash_index][0][1]])
            duplicate_counter += 1
            total_duplicates += table[hash_index][0][1]

    write_output_file("output.txt", f"{duplicate_counter}\n")
    write_output_file("output.txt", f"{total_duplicates}\n")
    write_output_file("output.txt", f"{unique_ids}\n")
  

    
    


if __name__ == "__main__":
    main()