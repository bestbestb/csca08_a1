# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: Zhengshuo Xu
# MarkUs Login: xuzheng
#

PUZZLE1 = '''
glkutqyu
onnkjoaq
uaacdcne
gidiaayu
urznnpaf
ebnnairb
xkybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyotiutuvpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)
# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.

    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    '''
    # call the lr_occurrences function to count
    result = lr_occurrences(puzzle, word)
    # call the rotate function to rotate
    puzzle1 = rotate_puzzle(puzzle)
    result1 = lr_occurrences(puzzle1, word)
    puzzle2 = rotate_puzzle(puzzle1)
    result2 = lr_occurrences(puzzle2, word)
    puzzle3 = rotate_puzzle(puzzle2)
    result3 = lr_occurrences(puzzle3, word)
    # add all the results
    total = result + result1 + result2 + result3
    return total

# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    '''(str,str) -> boolean
    Return True if and only if the given word can be found in the puzzle from
    left to right or right to left, otherwise return False.
    >>> in_puzzle_horizontal('aaxy\nyaaa', 'aa')
    True
    >>> in_puzzle_horizontal('acxy\nyada', 'ab')
    False
    >>> in_puzzle_horizontal('acxz\nbaaa', 'ab')
    True
    '''
    # count from left to right first
    result = lr_occurrences(puzzle, word)
    # rotate twice
    puzzle1 = rotate_puzzle(puzzle)
    puzzle2 = rotate_puzzle(puzzle1)
    # count from right to left
    result2 = lr_occurrences(puzzle2, word)
    # add the results and get total
    total = result + result2
    return (total >= 1)
        
 
# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    '''(str,str) -> boolean
    Return True if and only if the given word can be found in the puzzle from
    top to bottom or from bottom to top, otherwise return False.
    >>> in_puzzle_vertical('aaxy\nyaaa', 'aa')
    True
    >>> in_puzzle_vertical('acxy\nyada', 'ab')
    False
    >>> in_puzzle_vertical('acxz\nbaaa', 'ab')
    True
    '''
    # rotate once
    puzzle1 = rotate_puzzle(puzzle)
    # count from top to bottom first
    result1 = lr_occurrences(puzzle1, word)
    # rotate twice
    puzzle2 = rotate_puzzle(puzzle1)
    # rotate 3 times
    puzzle3 = rotate_puzzle(puzzle2)
    # count from bottom to top
    result3 = lr_occurrences(puzzle3, word)
    # add the results and get total
    total = result1 + result3
    return (total >= 1)
       

# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle(puzzle, word):
    '''(str,str) -> boolean
    Return True if and only if the given word can be found in the puzzle in
    either of the four directions, otherwise return False.
    >>> in_puzzle('aaxy\nyaaa', 'aa')
    True
    >>> in_puzzle('acxy\nyada', 'ab')
    False
    >>> in_puzzle('acxz\nbaaa', 'ab')
    True
    '''
    # call the total_occurrences function
    result = total_occurrences(puzzle, word)
    return result > 0
   

# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    '''(str,str) -> boolean
    Return True if and only if the given word can be found in the puzzle in
    either horizontal direction or vertical direction, but not both.
    Otherwise return False.
    >>> in_exactly_one_dimension('aaxy\ncaaa', 'ac')
    False
    >>> in_exactly_one_dimension('anxy\nyada', 'ab')
    False
    >>> in_exactly_one_dimension('acxz\nbaaa', 'ab')
    False
    '''
    # call the two functions
    vertical = in_puzzle_vertical(puzzle, word)
    horizontal = in_puzzle_horizontal(puzzle, word)
    #  word can only appear in either dimention but not both
    result= ((vertical >= 1) and (horizontal == 0)) or ((horizontal >= 1) and (vertical == 0))
    return result
   
    
   

# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    '''(str,str) -> boolean
    Return True if and only if all occurrences of the supplied word can be
    found in horizontal order only, otherwise return False.
    >>> all_horizontal('aaxy\ncaaa', 'ac')
    False
    >>> all_horizontal('anxy\nyada', 'ab')
    True
    >>> all_horizontal('acxz\nbaaa', 'ab')
    False
    '''
    # call the vertical funtion
    vertical = in_puzzle_vertical(puzzle, word)
    # as long as the vertical function returns 0 we can return True
    result = (vertical == 0)
    return result
     
# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    '''(str,str) -> boolean
    Return True if and only if all occurrences of the supplied word can be
    found in horizontal order only, otherwise return False.
    >>> at_most_one_vertical('aaxy\ncaaa', 'ac')
    False
    >>> at_most_one_vertical('anxy\nyada', 'ab')
    True
    >>> at_most_one_vertical('acxz\nbaaa', 'ab')
    False
    '''
    # call the total_occurrences function
    total = total_occurrences(puzzle, word)
    # call the in_puzzle_horizontal funtion
    horizontal = in_puzzle_horizontal(puzzle, word)
    # as long as the total function returns smaller or equal to 1 and
    # horizontal function returns 0 we return True
    result = (total <= 1) and (horizontal == 0)
    return result
    


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''

    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here
    result = lr_occurrences(puzzle, name)
    print (result)

    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    puzzle1 = rotate_puzzle(puzzle)
    result1 = lr_occurrences(puzzle1, name)
    print (result1)

    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.
    print('Number of times', name, 'occurs right-to-left: ', end='')
    puzzle2 = rotate_puzzle(puzzle1)
    result2 = lr_occurrences(puzzle2, name)
    print (result2)

    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    puzzle3 = rotate_puzzle(puzzle2)
    result3 = lr_occurrences(puzzle3, name)
    print (result3)

    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.
    print (total_occurrences(puzzle, name))

    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.
    print (in_puzzle_horizontal(puzzle, name))

do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')

# *task* 7: call do_tasks on PUZZLE2 (that's a 2!) and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, 'nick')

# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print (in_puzzle(PUZZLE1, 'nick'))

# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'anya'.
# Add only one line below. Your code should print only True or False.
print (in_puzzle(PUZZLE2, 'nick'))
