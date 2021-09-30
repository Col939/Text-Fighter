import random
import time
import sys

#enemyTypes = ["Ground", "Flying", "Water"]

class Enemy:
    health = random.randint(5, 20)
    if health > 10:
        attPower = random.randint(2, 6)
    else:
        attPower = random.randint(5, 10)
    dfc = 1
    speed = random.randint(1, 5)    
    #eType = random.choice(enemyTypes)

class Player:
    health = 100
    attPower = 1
    dfc = 50
    speed = 1
    mana = 10
    gold = 0

turn = "p"

moves = ["attack"]

classes = ["Healer", "Warlock", "Mage", "Trader"]
classDescriptions = ["You heal hp every turn", "Your damage has a chance of being a critical strike", 
"Your mana recharges twice as fast", "Shop prices are halved"]
selClass = ""

manaMoves = ["Fireball", "Lightning Strike", "Wave of Pain"]
manaCosts = [8, 12, 16]
manaMoveStrenth = [5, 10, 15]
unlockedManaMoves = ["Fireball"]

shopItems = ["Potion of Healing", "Potion of Leveling", "Potion of Mana"]
shopItemDescriptions = ["Heals the player by 25 hp, tastes like cherries", "Grants the player the remaining xp to level up",
"Recharges the players mana by 20 points"]
shopItemCosts = [50, 600, 75]

fullHealth = 100

fullMana = 10

moveNum = 1

roundNum = 1

manaRechargeCount = 2
healthRechargeCount = -1

lvlNum = 1

xpNeeded = 100
xpGained = 0

oldXpGained = 0

shopOpenCount = 0
goldGained = 0

minLvlUp = 1
maxLvlUp = 3

block = False


    
    
name = input("What is your name?\n");
if name == "Jakob":
    print("You died")
    sys.exit()

    


def shopOpen():
    global shopOpenCount
    global player
    shopOpenCount += 1
    print("\033c")
    index = 0
    print("Type the type of potion in LOWERCASE to buy, or type leave to leave the shop. Ex. typing healing will buy a Potion of Healing")
    for x in shopItems:
        print("\n" + x + ": " + str(shopItemCosts[index]) + "g\n" + shopItemDescriptions[index])
        index += 1
    i = input("")
    print("\033c");
    if i == "healing" and player.gold >= shopItemCosts[0]:
        if player.health + 25 > fullHealth:
            print("You gain " + str(fullHealth - player.health) + "hp");
            player.health += fullHealth - player.health;
        else:
            player.health += 25;
            print("You gained 25 hp")
        print("Your mom left you at birth you waste of space")
    time.sleep(5);
    print("\033c");
    nextBattle()


def levelUp():
    global player
    global lvlNum
    global xpNeeded
    global fullHealth
    global xpGained
    global fullMana
    
    xpNeeded *= 1.5
    xpGained = 0
    lvlNum += 1
    
    
    print("\033c")
    print("Which stat would you like to increase?")
    x = input("a to increase attack, d to increase defense, s to increase speed, h to increase health, m to increase mana \n")
    lvlUpValue = random.randint(minLvlUp, maxLvlUp)
    if x == "a":
        player.attPower += lvlUpValue
        print("Your attack was increased by " + str(lvlUpValue))
        
    elif x == "d":
        player.dfc += lvlUpValue
        print("Your defense was increased by " + str(lvlUpValue))
        
    elif x == "s":
        player.speed += lvlUpValue
        print("Your speed was increased by " + str(lvlUpValue))
        
    elif x == "h":
        player.health = fullHealth
        player.health += (lvlUpValue + 5)
        fullHealth += (lvlUpValue + 5)
        print("Your health was set back to full and increased by " + str(lvlUpValue + 5))
        
    elif x == "m":
        player.mana = fullMana
        player.mana += (lvlUpValue + 3)
        fullMana += (lvlUpValue + 5)
        
    time.sleep(2)
    print("\033c")
    if lvlNum == 2:
        classAssign()
    

def classAssign():
    global selClass
    print("\033c")
    index = 0
    for x in classes:
        print(x + "\n" + classDescriptions[index] + "\n")
        index += 1
    print("\nType the first letter of the class you want to select in LOWERCASE \nWarning: Your class CANNOT be changed unless you restart the game")
    i = input("")
    if i == "h":
        selClass = "Healer"
    elif i == "w":
        selClass = "Warlock"
    elif i == "m":
        selClass = "Mage"
    elif i == "t":
        selClass = "Trader"
    time.sleep(.5)
    print("\033c")
    
    
def recharge():
    global manaRechargeCount
    global healthRechargeCount
    global player
    
    manaRechargeCount -= 1
    if manaRechargeCount == 0:
       if selClass == "Mage":
         manaRechargeCount = 1
       else:
         manaRechargeCount = 2
       if (player.mana + 1) <= fullMana:
          player.mana += 1
          print("The Mages Mark increased your mana by 1")
       else:
          print("Your mana is full")
    if selClass == "Healer":
        
        if (player.health + 2) < fullHealth:
            player.health += 2
            print("The Healers Hat increased your health by 2")
        elif (player.health + 1) == fullHealth:
            player.health += 1
            print("The Healers Hat increased your health by 1")
            
    print("Health: " + str(player.health))
    print("Mana: " + str(player.mana))
    time.sleep(2)
    print("\033c")
    
    
def nextBattle():
    global player
    global enemy
    global turn
    global moveNum
    global roundNum
    global block
    
    enemy = Enemy()
    if enemy.speed > player.speed:
        turn = "e"
    else:
        turn = "p"
    block = False
    roundNum += 1
    moveNum = 1
    
    if roundNum % 2 == 0:
        shopOpen()
    else:  
        battleSequence()
    

def battleSequence():
    global player
    global enemy
    global turn
    global moveNum 
    global roundNum
    global xpGained
    global xpNeeded
    global block
    global oldXpGained

    block = False
    
    if roundNum == 1:
        enemy.health = 1
        enemy.attPower = 1
        enemy.speed = 1
        enemy.dfc = 1
        #enemy.eType = enemyTypes[0]
        
    
    if moveNum == 1:
        print("You encountered an enemy!")
        print("\nLevel: " + str(lvlNum))
        print("Round Number: " + str(roundNum))
        time.sleep(1.5)
        print("\033c")
    
    if turn == "p":

        move = input("What do you do? \n" + "Type a to attack, b to block, m to use a magic attack, or r to run \nMana: " + str(player.mana) + "\n")
        
        print("\033c")
        moveNum += 1 
        if move == "a":
            enemy.health -= player.attPower
            turn = "e"
            time.sleep(1.5)
            print("Enemy Health: " + str(enemy.health))
          

        
        elif move == "b":
            c = random.randint(1, 100);
            if c < player.dfc:
                block = True
            else:
                block = False
            turn = "e"
            
        elif move == "m":
            print("\033c")
            print("Type the first and last letter of the move to activate it or type back to go back\n")
            index = 0
            for x in unlockedManaMoves:
                print(x + "; Cost: " + str(manaCosts[index]))
                index += 1
            moveUsed = input("")
            
            if moveUsed == "fl":
                if player.mana >= manaCosts[0]:
                    print("\033c")
                    print("A blazing fireball struck the enemy")
                    enemy.health -= manaMoveStrenth[0]
                    player.mana -= manaCosts[0]
                else:
                    print("\033c")
                    print("You dont have enough mana to use this move :(")
                    time.sleep(1.5)
                    print("\033c")
                    battleSequence()
                    return
            
            if moveUsed == "back":
                print("\033c")
                battleSequence()
                return
                
            turn = "e"
            time.sleep(1.5)
            print("Enemy Health: " + str(enemy.health))
            
    if enemy.health <= 0:
        if roundNum == 1:
            xpGained = 100
            goldGained = 10
        else:
            oldXpGained = xpGained
            xpGained += random.randint(lvlNum, lvlNum * 100)
            goldGained = random.randint(lvlNum, lvlNum * 50)
            player.gold += goldGained
        print("You killed the enemy!")
        print("\nYou gained " + str(xpGained - oldXpGained) + "xp")
        print("You found " + goldGained + " gold")
        

        if xpNeeded <= xpGained:
            print("You leveled up!")
            time.sleep(1.7)
            levelUp()
        else:
            print(str(xpNeeded - xpGained) + " is needed to level up")
            time.sleep(1.7)
            print("\033c")
        nextBattle()
        return
            
    if turn == "e":
        x = random.choice(moves)
        if x == "attack":
            if block == False:
                print("The enemy attacked you for " + str(enemy.attPower) + "\n")
                player.health -= enemy.attPower
                time.sleep(1.5)
                if player.health <= 0:
                    print("Game Over")
                    time.sleep(2)
                    return False
                else:    
                    print("Player Health: " + str(player.health) + "\n")
            else:
                print("The enemys attack was blocked")
            turn = "p"
            time.sleep(1.5)
            print("\033c")
     
    recharge()
    
    battleSequence()

def startRound():
    global player
    global enemy
    global turn
    player = Player()
    enemy = Enemy()
    print("\033c")
    battleSequence()
startRound()
