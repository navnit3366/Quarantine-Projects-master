import random

# To print the faces of dice
d1 = "-------"
d2 = "|    O|"
d3 = "|  O  |"
d4 = "|O    |"
d5 = "|O   O|"
d6 = "|O O O|"
d7 = "|     |"

# The dice
r1 = [d1, d7, d3, d7, d1]
r2 = [d1, d2, d7, d4, d1]
r3 = [d1, d4, d3, d2, d1]
r4 = [d1, d5, d7, d5, d1]
r5 = [d1, d5, d3, d5, d1]
r6 = [d1, d6, d7, d6, d1]
dice = [r1, r2, r3, r4, r5, r6]

running = True
print("Welcome to the world of dice. Would you like to roll one?\nEnter Y for yes or any other key to exit.")
inp = input()
if inp == "Y" or inp == "y":
    running = True
else:
    running = False

# The player turns the dice here
while running:
    c = random.randint(0, 5)
    die = dice[c]
    for i in die:
        print(i)
    print("Do you want to roll again?\nEnter Y for yes or any other key to exit.")
    inp = input()
    if inp == "Y" or inp == "y":
        running = True
    else:
        running = False
