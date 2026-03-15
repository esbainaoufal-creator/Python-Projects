name = input("chose your character name >>")
health = 100
Goblen_health = 50
player_alive = True
Orc_health = 80
print("You are in the desert !")
print("A goblen has spawned!!")

while True:
    print("1. attack!")
    print("2. avoid!")
    attack = int(input("What would you do? >>"))

    match attack:
        case 1:
            health = health - 15
            Goblen_health = Goblen_health - 25
            print("You attacked the goblen!")
            print("Your health is " + str(health))
        case 2:
            health = health - 5
            print("You avoided but goblen still hit you!")
            print("Your health is " + str(health))

    if Goblen_health <= 0:
        print("The goblen is dead! You won!!")
        with open("RPG_Progress.txt", "w") as f :
                f.write(name + " You Won! You killed the Goblen!")  
        break

    if health <= 0:
        print("You are dead! Game over!!")
        player_alive = False
        with open("RPG_Progress.txt", "w") as f :
                f.write(name + " You lost! The goblen killed you!")  
        break

if player_alive:
    print("You went deep into the desert!")
    print("You found a bottle of some elexir!")
    print("1. drink it!")
    print("2. throw it!")
    choice = int(input("what would you do? >>"))
    match choice:
        case 1:
            health = 100
            print("nice choice! you got rehealed!")
        case 2:
            print("It was healing elexir! your health still " + str(health))
    print("OH NOO!")
    print("an Orc has spawned!")
    print("You can:")
   
    while True:
        print("1. fight!")
        print("3. Run!")
        choice = int(input("what would you do? >>"))
        match choice:
            case 1:
                health = health - 20
                Orc_health = Orc_health - 30
                print("You attacked the Orc!")
                print("Your health is " + str(health))
            case 3:
                health = 0
                print("You lost in the desert and died from starvation and thirst")
        if Orc_health <= 0:
            print("The Orc is dead! You won!!")
            with open("RPG_Progress.txt", "w") as f :
                f.write(name + " You won! You killed the Orc!")  
            break

        if health <= 0:
            print("You are dead! Game over!!")
            player_alive = False
            with open("RPG_Progress.txt", "w") as f :
                f.write(name + " You lost! The Orc killed you!")  
            break   
        
 
