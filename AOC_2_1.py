print("Advent of Code Day 2 Exercise 1")

# Set local variables
mylist = []
score = int(0)

f = open("/Users/pauldobe/AOC_22/input_file_day_2", "r")
for x in f:
    y = x.split()
    mylist.append(y)

for x in mylist:
    if x[0] == "A":
        if x[1] == "X":
            score = score + 4
        elif x[1] == "Y":
            score = score + 8
        elif x[1] == "Z":
            score = score + 3  
    elif x[0] == "B":
        if x[1] == "X":
            score = score + 1
        elif x[1] == "Y":
            score = score + 5
        elif x[1] == "Z":
            score = score + 9
    elif x[0] == "C":
        if x[1] == "X":
            score = score + 7
        elif x[1] == "Y":
            score = score + 2
        elif x[1] == "Z":
            score = score + 6

print ("Final score is: " + str(score))

f.close
