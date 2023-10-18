import random
from time import*
def dragon_slayer(dragon_stats, player_stats):
    difficulty = input("WELCOME TO DRAGONSLAYER, CHOOSE YOUR DIFFICULTY :\nEASY - 1\nMEDIUM - 2\nHARD - 3\n")
    if difficulty == "1":
        dragon_health = dragon_stats["health"] - 20
        dragon_attack = dragon_stats["attack"] - 1
        dragon_defense = dragon_stats["defense"] - 1
    
        player_health = player_stats[0]
        player_attack = player_stats[1]
        player_defense = player_stats[2]
    elif difficulty == "2":
        dragon_health = dragon_stats["health"] 
        dragon_attack = dragon_stats["attack"]
        dragon_defense = dragon_stats["defense"]
    
        player_health = player_stats[0]
        player_attack = player_stats[1]
        player_defense = player_stats[2]
    elif difficulty == "3":
        dragon_health = dragon_stats["health"] + 10
        dragon_attack = dragon_stats["attack"] + 1
        dragon_defense = dragon_stats["defense"] + 1
    
        player_health = player_stats[0]
        player_attack = player_stats[1]
        player_defense = player_stats[2]
    print()
    print("-------------------------------------------")
    print("You are about to face a  dangerous dragon, but all of a sudden, an old lady appears in front of you and says:")
    print('"Ill give you these potions, you will definetely need them."')
    print("*you gained: potion of strength, healing potion, stealth potion*")
    print("-------------------------------------------")
    print("A fearsome dragon appears!")
    potions = ["potion of strength", "healing potion", "stealth potion"]
    attack = 0
    potion_empty = 0
    attack_dragon = 0
    empty = False 
    strength_potion = False
    stealth_potion = False 
    
    while True:

        print("Dragon's health:", dragon_health)
        print("Player's health:", player_health)
        print()
        
        # Player's turn
        print("Player's turn:")
        print("1. Attack")
        print("2. Defend")
        print("3. Drink a potion")
        print()
        choice = input("Choose your move (1 or 2 or 3): ")
        if choice == "3":
            if potion_empty == 3:
                empty = True
            if empty == True:
                print("you have no more potions in your backpack.")
                continue
            
            print("Potions in your backpack:")
            print()
            for potion in potions:
                print(potion)
                print()
            print("which of them do you want to use?")
            print()
            if "potion of strength" in potions:
                print("potion of strength : 1")
            if "healing potion" in potions:
                print("healing potion : 2")
            if "stealth potion" in potions:
                print("stealth potion : 3")
            potion_choice = input()
            if (potion_choice == "1") and ("potion of strength" in potions):
                potion_empty += 1
                print("you decided to take the strength potion and do some more damage!")
                print("*critical hit chance increased for four attacks*")
                strength_potion = True
                potions.remove("potion of strength")
            elif (potion_choice == "2") and ("healing potion" in potions):
                potion_empty += 1 
                print("you decided to take the healing potion and heal yourself!")
                print("*you gained 15 health*")
                player_health += 15
                if player_health > 70:
                    player_health = 70
                print(f"your health is now {player_health}")
                potions.remove("healing potion")
            elif (potion_choice == "3") and ("stealth potion" in potions):
                potion_empty += 1
                print("you decided to take the stealth potion and be more sneaky!")
                print("*dragon miss chance has increased for five rounds*")
                stealth_potion = True
                potions.remove("stealth potion")
        elif choice == "1":
            print("Players attack:")
            player_attack = random.randint(0, player_attack)
            player_damage = player_attack - dragon_defense
            miss_chance_player = random.randint(0, 15)
            critical_hit_chance = random.randint(10, 20)
            if miss_chance_player >= 14:
                print("unfortunately, you missed your attack!")
            elif strength_potion == True:
                player_damage += 2
                critical_hit_chance = random.randint(10, 12)
                if (player_damage > 0) and (critical_hit_chance == 11):
                    print("Nice! You managed to deal a critical hit to the dragon!")
                    player_damage += random.randint(5, 10)
                    dragon_health -= player_damage 
                    print("You deal", player_damage, "damage to the dragon!")
                    
                elif (player_damage > 0) and (critical_hit_chance != 13):
                    dragon_health -= player_damage
                    print("You deal", player_damage, "damage to the dragon!")
                else:
                    print("this attack was too weak to penetrate the dragon's defenses.")
                attack += 1
                if attack == 5:
                    print("*your potion of strength has run out*")
                    strength_potion = False
            elif (player_damage > 0) and (critical_hit_chance > 18):
                print("Nice! You managed to deal a critical hit to the dragon!")
                player_damage += random.randint(5, 10)
                dragon_health -= player_damage 
                print("You deal", player_damage, "damage to the dragon!")
            elif player_damage > 0:
                dragon_health -= player_damage
                print("You deal", player_damage, "damage to the dragon!")
            else:
                print("this attack was too weak to penetrate the dragon's defenses.")
        elif choice == "2":
            player_defense += 5
            print("You brace yourself for the dragon's attack.")
        else:
            print("invalid move")
            print()
            continue
        if dragon_health <= 0:
            print("You have slain the dragon! Congratulations!")
            break
            
        # Dragon's turn
        print()
        print("Dragon's attack:")
        miss_chance_dragon = random.randint(0, 15)
        dragon_attack = random.randint(0,dragon_attack)
        dragon_damage = dragon_attack - player_defense
        if stealth_potion == True:
            miss_chance_dragon = random.randint(10, 12)
            if miss_chance_dragon == 11:
                print("nice! the dragon missed his shot.")
            elif miss_chance_dragon != 11:
                dragon_attack = random.randint(0,dragon_attack)
                dragon_damage = dragon_attack - player_defense
                if dragon_damage <= 0:
                    print("The dragon's attack was too weak to penetrate your defenses.")
                else:
                    player_health -= dragon_damage
                    print("The dragon deals", dragon_damage, "damage to you!")
            attack_dragon += 1
            
                

            if attack_dragon == 5:
                print("your stealth potion has ran out.")
                stealth_potion = False 

        elif miss_chance_dragon >= 13:
            print("nice! the dragon missed his shot.")
        elif dragon_damage > 0:
            player_health -= dragon_damage
            print("The dragon deals", dragon_damage, "damage to you!")
        else:
            print("The dragon's attack was too weak to penetrate your defenses.")
        
        if player_health <= 0:
            print("You have been defeated by the dragon. Game over.")
            break
        
        # Reset player's defense
        player_defense  //= 2
        player_attack = player_stats[1]
        dragon_attack = dragon_stats["attack"]
        
        # Pause for dramatic effect
        print("------------------------")


dragon_stats = {
    "health": 100
    ,
    "attack": 9,
    "defense": 3}

player_stats = (70, 12, 5)

dragon_slayer(dragon_stats, player_stats)