try:
    with open("progress.txt", "r") as f:
        streak = int(f.read())
except:
    streak = 0

while True:
            answear = input("Did you wash your hands Today? (Yes or No) >> ")
            if answear == "No" or answear == "no":
                streak = 0
                print("Your streak is reseted, try harder!")
            elif answear == "Yes" or answear == "yes":
                streak += 1
                if streak == 1 :
                    print("Good Job! your streak is now  : " + str(streak) + " day!")
                
                else:
                    print("Good Job! your streak is now : " + str(streak) + " days!")
            with open("progress.txt", "w") as f :
                f.write(str(streak))