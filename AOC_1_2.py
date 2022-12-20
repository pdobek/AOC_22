print("Advent of Code Day 1 Exercise 2")

# Set local variables
y = int(0)
calories = int(0)
count = int(0)
calorielist = []

f = open("/Users/pauldobe/AOC_22/input_file_day_1", "r")
for x in f:
    if x != "\n":
        y = y + int(x)
    else:
        calorielist.append(y)
        y = 0

calorielist.sort(reverse = True)

calories = calorielist[0] + calorielist[1] + calorielist[2] 

print(calories)

f.close

ß