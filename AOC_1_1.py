print("Advent of Code Day 1 Exercise 1")

# Set local variables
y = int(0)
maxy = int(0)

f = open("/Users/pauldobe/AOC_22/input_file_day_1", "r")
for x in f:
    if x != "\n":
        y = y + int(x)
    else:
        if y > maxy:
            maxy = y
            print("New max is " + str(maxy))
            y = 0
        else:
            print("Max is still " + str(maxy))
            y = 0


print("The elf carrying the most calories is carrying: ")
print(maxy)

f.close

