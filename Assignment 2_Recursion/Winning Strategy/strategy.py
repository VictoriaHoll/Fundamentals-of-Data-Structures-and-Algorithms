# 1b Fundamentals of Data Structures and Algorithms

# Assignment 2, Winning Strategy

# n = input('Provide the starting state of the game, N:')

def is_hot(n):  
    if n < 2:
        game_state = 'cold'
        return game_state
    
    option_1 = is_hot(n-1)
    option_2 = is_hot(n/2)
    
    if option_1 == 'hot' and option_2 == 'hot':
        game_state = 'cold'
        return game_state
    else:
        game_state = 'hot'
        return game_state

input_file = open("input.txt", "r")
output_file = open("output.txt","w+")

for line in input_file.readlines():
    line_modified = line.rstrip('\n')
    output_file.write(is_hot(int(line_modified)))
    output_file.write('\n')
    
input_file.close()
output_file.close()