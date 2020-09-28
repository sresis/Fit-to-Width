"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""
    # store current line length
    # store current line
    # before it exceeds it, print it and reset
    #how to handle if it doesn't exceed
    #how to get the last line
    str_list = string.split(' ')
    line_len = 0
    current_line = ''
    all_lines = []
    # if this is the last line
    char_count = 0
    for item in str_list:
        char_count += len(item)
    
    
    if char_count < limit:
        print(string)
        return
    for item in str_list:
        if len(item) + len(current_line) <= limit:
            current_line += item + ' '
        
        else:
            if current_line[-1] == ' ':
                print(current_line[:-1])

            else:
                print(current_line)
            current_line = item + ' '
    # print last row
    if current_line[-1] == ' ':
        print(current_line[:-1])

    else:
        print(current_line)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
