# 1b Fundamentals of Data Structures and Algorithms

# Assignment 2, Scramble


def interleave(string1, string2):
    new_string = ''
    string1_length = len(string1)
    i = 0
    while i < string1_length:
        new_string += string1[i]
        new_string += string2[i]
        i += 1
    return new_string

def even_harder(string):
    # Single character string
    if len(string) <= 2:
        return string
    
    # Find out if string has length to the power of 2
    total_length = len(string)
    new_string = string 
    i = 0
    while True:
        if total_length == 2: 
            break
        elif (total_length / 2) % 2 == 0: # Checks if half is even
            total_length /= 2
    
    # If string is not to the power of 2, modify it with '.' until it is:
        else:
            new_string += '.'
            total_length = len(new_string)
    
    # Once string is to the power of 2, split in half
    S1 = new_string[0:len(new_string)//2]
    S2 = new_string[len(new_string)//2:]
    
    # Interleave within each half
    rec1 = even_harder(S1)
    rec2 = even_harder(S2)
    A1 = interleave(rec1, rec2)

    # Return interleave of both halfs
    return A1

input_file = open("input.txt", "r")
output_file = open("output.txt","w+")
# print(input_file.readlines())
# print(input_file.readline())

for line in input_file.readlines():
    line_modified = line.rstrip('\n')
    output_file.write(even_harder(str(line_modified)))
    output_file.write('\n')
    
input_file.close()
output_file.close()
