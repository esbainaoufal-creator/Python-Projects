import random
print("                  ------- Welcome To Guess the chosen --------")
print("                  =======      We chose YOU guess    =========")
print("      we gonna tell you if you're guess is higher or lower than the number we chose")
print("                       the numbers are from 1 to 100")
print("                                Let's Go!")
number = random.randint(1, 100)
count = 0
while True:
    guess = int(input("Insert a guess>> "))
    count += 1
    if guess == number:
        print("You got it!")
        break
    elif number > guess:
        print("Higher!")
        continue
    else:
        print("Lower")
        continue

print("You did " + str(count) + " attempts!")