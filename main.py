# regular expression library that helps us manipulate strings
# used it to create a list of integers from in4c.txt
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

    # my algorithm ia everything below this

    # my hash function
    def my_hash_function(key, table_size):
        return key % table_size
    
    # from here you can update the size of the table
    table_size = 30
    # create hash table of size "table_size"
    table = [[] for _ in range(table_size)]
    # variable to count all duplicates, even the repeated ones
    total_duplicates_count = 0
    # variable to keep track of all IDs, even repeated ones
    total_ids = 0

    # looping through identifications keep track ofo count of every number
    # in the list
    for element in identifications:
        # obtain a hash_index for all numbers in list, so we
        # can add them to our hash table "table"
        hash_index = my_hash_function(element, table_size)

        # if element is not at hash_index, add element to "table"
        if not table[hash_index]:
            table[hash_index]. append([element, 1])
            # keeping track of total number of ids
            total_ids += 1

        # if element does NOT equal element at hash_index, we loop
        # through the row to find it, if not, we add element to row (separate chaining)
        #         [   row    ][index at row][key]
        elif table[hash_index][      0     ][ 0 ] != element:
            found = False
            # look for element in row
            for item in table[hash_index]:
                if item[0] == element:
                    item[1] += 1
                    found = True
            # if element not found in row, add it to the end of row
            if found == False:
                table[hash_index][0].append([element, 1])
            # keeping track of total number of ids
            total_ids += 1
        
        # if element DOES EQUAL element at hash_index, increment value by 1
        else:
            #    [   row    ][index at row][value]
            table[hash_index][      0     ][  1  ] += 1
            # keeping track of total number of ids
            total_ids += 1


    # we basically loop through identifications list a second time to print duplicates
    # (in order of first appearance)

    # we create another hash table to keep track of what duplicate
    # we have already printed, so we dont double-print
    keep_track_of_prints = [[] for _ in range(table_size)]
    # variable to count the unique duplicates that there are
    unique_duplicates_count = 0

    # this is where we begin writing to file
    write_output_file("output.txt", "Duplicates found (in order of first appearance): \n")
    for element in identifications:
        # we hash elements to avoid printing duplicates twice
        hash_index = my_hash_function(element, table_size)
        # we look for element in row if not in the first index
        #        [   row   ][index at row][key]
        if table[hash_index][      0     ][ 0 ] != element:
            # look for element in row
            for item in table[hash_index]:
                # if element is in row and is a duplicate, and if we have
                # not printed it yet, print it
                if item[0] == element and item[1] > 1 and not keep_track_of_prints[hash_index]:
                    write_output_file("output.txt", f"{element} -> appears {item[1]} times\n")
                    keep_track_of_prints[hash_index].append([element, item[1]])
                    unique_duplicates_count += 1
                    total_duplicates_count += item[1]
            
        # we print element only if it is a duplicate, and if we have not printed it yet
        #       [   row    ][index at row][key]
        if table[hash_index][      0     ][ 0 ] == element and table[hash_index][0][1] > 1 and not keep_track_of_prints[hash_index]:
            write_output_file("output.txt", f"{element} -> appears {table[hash_index][0][1]} times\n")
            keep_track_of_prints[hash_index].append([element, table[hash_index][0][1]])
            unique_duplicates_count += 1
            total_duplicates_count += table[hash_index][0][1]

    # we use our other counter variable to calculate the total unique IDs
    # in our list
    unique_ids = (total_ids - total_duplicates_count) + unique_duplicates_count
    # we print total unique IDs and total duplicate IDs
    write_output_file("output.txt", f"Total Unique IDs: {unique_ids}\n")
    write_output_file("output.txt", f"Total Duplicate IDs: {unique_duplicates_count}\n")

    
# main
if __name__ == "__main__":
    main()