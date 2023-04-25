# Let user input line
starting_line = input("Good Day! input your this program will let you input lines. Please input your first line: ")
# Enter line 1 to mylife.txt
with open("mylife.txt", "w") as my_life_line:
    my_life_line.write(starting_line)
# let user choose to write more lines
line_2_decision = input("Are there more lines? y/n: ")
# Enter line 2
# let user choose to write more lines
# Enter line 3
# enter all line to mylife.txt