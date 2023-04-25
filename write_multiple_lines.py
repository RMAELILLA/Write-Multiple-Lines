# Let user input line
starting_line = input("Good Day! input your this program will let you input lines. Please input your first line: ")
# Enter line 1 to mylife.txt
# let user choose to write more lines
line_2_decision = input("Are there more lines? y/n: ")
if line_2_decision == "y":
    # Enter line 2
    second_line = input("What is your Second line? : ")
else:
    second_line = input(("Please continue, what is your second line? : "))

# let user choose to write more lines
line_3_decision = input("Are there more lines? y/n: ")
if line_3_decision == "y":
    # Enter line 3
    third_line = input("What is your Third line? : ")
else:
    third_line = input(("Please continue, what is your third line? : "))

input("Are there more lines? y/n: ")
# enter all line to mylife.txt
with open("mylife.txt", "w") as my_life_line:
    my_life_line.write(starting_line + "\n" + second_line + "\n" + third_line + "\n")