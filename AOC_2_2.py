print("Advent of Code Day 2 Exercise 2")

# Set local variables
mylist = []
score = int(0)

f = open("/Users/pauldobe/AOC_22/input_file_day_2", "r")
for x in f:
    y = x.split()
    mylist.append(y)

for x in mylist:
    if x[0] == "A": # ROCK
        if x[1] == "X": #LOSE -> SCISSORS
            score = score + 3
        elif x[1] == "Y": #DRAW -> ROCK
            score = score + 4
        elif x[1] == "Z": #WIN -> PAPER
            score = score + 8  
    elif x[0] == "B": # PAPER
        if x[1] == "X": #LOSE -> ROCK
            score = score + 1
        elif x[1] == "Y": #DRAW -> PAPER
            score = score + 5
        elif x[1] == "Z": #WIN -> SCISSORS
            score = score + 9
    elif x[0] == "C": # SCISSORS
        if x[1] == "X": #LOSE -> PAPER
            score = score + 2
        elif x[1] == "Y": #DRAW -> SCISSORS
            score = score + 6
        elif x[1] == "Z": #WIN -> ROCK
            score = score + 7

print ("Final score is: " + str(score))

f.close
