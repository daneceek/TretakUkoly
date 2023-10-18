import random
from time import*
player_stats = (20, 8, 4)
dragon_stats = (30, 6, 2)
dragon_attack = 1

print("Welcome to Dragon Slayer!")
sleep(1)
print("You are about to face a mighty dragon in a battle to the death.")
sleep(1)
print("\nyour stats:")
print("-------------")
print(f"lives: {player_stats[0]}\ndamage: {player_stats[1]}\ndefense: {player_stats[2]}")
print("-------------")
sleep(1)
print("dragons stats:")
print("-------------")
print(f"lives: {dragon_stats[0]}\ndamage: {dragon_stats[1]}\ndefense: {dragon_stats[2]}")
print("-------------")

while True:
    move = int(input("Choose your move: 1 for attack, 2 for defend (dragon will deal less damage)\n"))
    
    if move == 1:
        damage = random.randint(1, player_stats[1])
        print("-------------")
        print(f"your attack : {damage}")
        print(f"dragon defense : {dragon_stats[2]}")
        print("-------------")
        sleep(1.5)
        if damage <= dragon_stats[2]:
            print("dragon blocked your damage.")
        else:
            damagetodragon = damage - dragon_stats[2]
            dragon_stats = (dragon_stats[0] - damagetodragon, dragon_stats[1], dragon_stats[2])
            print(f"You attack the dragon and deal {damagetodragon} damage!")
            sleep(0.5)
            if dragon_stats[0] <= 0:
                print("dragon now has 0 lives!")
                print("Congratulations, you have slain the dragon and saved the kingdom!")
                break
            print(f"dragon now has {dragon_stats[0]} lives.")

    elif move == 2:
        player_stats = (player_stats[0], player_stats[1], player_stats[2] + 1)
      
        print("You defend yourself and increase your defense by 1!")
        sleep(1)
        print(f"your defense is now {player_stats[2]} ")
    else:
        print("Invalid move! Please try again.")
        continue
    print("-------------")
    print("Now it's dragons turn.")
    sleep(1)
    dragon_damage = random.randint(0, dragon_stats[1])
    print("-------------")
    print(f"dragons attack : {dragon_damage}")
    print(f"your defense : {player_stats[2]}")
    print("-------------")
    sleep(1.5)
    if dragon_damage <= player_stats[2]:
        print("you blocked dragons attack!")
    else:
        damagetoplayer = dragon_damage - player_stats[2]
        player_stats = (player_stats[0] - damagetoplayer, player_stats[1], player_stats[2])
        print(f"The dragon attacks you and deals {damagetoplayer} damage!")
        if player_stats[0] <= 0:
            print("You have been defeated by the dragon. Better luck next time!")
            break
        print(f"your lives: {player_stats[0]}")
        print("-------------")
        sleep(1)
    dragon_stats = (dragon_stats[0], dragon_stats[1] + 1, dragon_stats[2])
    print(f"dragons max. damage has increased by 1! It's now {dragon_stats[1]}")
    print("-------------")
    
import string