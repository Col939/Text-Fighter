import random
import time

class Enemy:
    health = random.randint(5, 20)
    if health > 10:
        attPower = random.randint(2, 6)
    else:
        attPower = random.randint(5, 10)
    dfc = 1
    speed = random.randint(1, 5)    

class Player:
    health = 100
    attPower = 1
    dfc = 50
    speed = 1
    mana = 10

turn = "p"

moves = ["attack"]

classes = ["Healer", "Warlock", "Mage"]
cDescriptions = ["You heal hp every turn", "Your damage has a chance of being a critical strike", "Your mana recharges twice as fast"]

manaMoves = ["Fireball", "Lightning Strike", "Wave of Pain"]
manaCosts = [8, 12, 16]
manaMoveStrenth = [5, 10, 15]
unlockedManaMoves = ["Fireball"]

fullHealth = 100

fullMana = 10

moveNum = 1

roundNum = 1

lvlNum = 1

xpNeeded = 100
xpGained = 0

oldXpGained = 0

minLvlUp = 1
maxLvlUp = 3

block = False

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
        
    time.sleep(3)
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
        

    if turn == "p":

        if moveNum == 1:
            print(enemy.health)

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
            print("Type the first and last letter of the move to activate it")
            index = 0
            for x in unlockedManaMoves:
                print(x + "; Cost: " + str(manaCosts[index]))
                index += 1
            moveUsed = input("")
            
            if moveUsed == "fl":
                enemy.health -= manaMoveStrenth[0]
                player.mana -= manaCosts[0]
                
            turn = "e"
            time.sleep(1.5)
            print("Enemy Health: " + str(enemy.health))
            
    if turn == "e":
        x = random.choice(moves)
        if x == "attack":
            if block == False:
                print("The enemy attacked you for " + str(enemy.attPower) + "\n")
                player.health -= enemy.attPower
                time.sleep(1.5)
                print("Player Health: " + str(player.health) + "\n")
            else:
                print("The enemys attack was blocked")
            turn = "p"
            time.sleep(1.5)
            print("\033c")
     
    
    if enemy.health <= 0:
        if roundNum == 1:
            xpGained = 100
        else:
            oldXpGained = xpGained
            xpGained += random.randint(lvlNum, lvlNum * 100)
        print("You killed the enemy!")
        print("\nYou gained " + str(xpGained - oldXpGained) + "xp")

        if xpNeeded <= xpGained:
            print("You leveled up!")
            time.sleep(2)
            levelUp()
        else:
            print(str(xpNeeded - xpGained) + " is needed to level up")
            time.sleep(2)
            print("\033c")
        nextBattle()
        return
    
    battleSequence()

def startRound():
    global player
    global enemy
    global turn
    player = Player()
    enemy = Enemy()
    battleSequence()
startRound()
