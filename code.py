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

turn = "p"

moves = ["attack"]

fullHealth = 100

moveNum = 1

roundNum = 1

lvlNum = 1

xpNeeded = 100
xpGained = 0

minLvlUp = 1
maxLvlUp = 3

block = False

def levelUp():
    global player
    global lvlNum
    global xpNeeded
    global fullHealth

    print("\033c")
    print("Which stat would you like to increase?")
    x = input("a to increase attack, d to increase defense, s to increase speed, h to increase health \n")
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
        player.health += lvlUpValue
        fullHealth += lvlUpValue
        print("Your health was set back to full and increased by " + str(lvlUpValue))
    time.sleep(3)
    print("\033c")

def battleSequence():
    global player
    global enemy
    global turn
    global moveNum 
    global roundNum
    global xpGained
    global xpNeeded
    global block

    block = False
    
    if roundNum == 1:
        enemy.health = 1
        enemy.attPower = 1
        enemy.speed = 1
        enemy.dfc = 1
        

    if turn == "p":

        if moveNum == 1:
            print(enemy.health)

        move = input("What do you do? \n" + "Type a to attack, b to block, or r to run \n")
        print("\033c")
        
        if move == "a":
            enemy.health -= player.attPower
            turn = "e"
            time.sleep(1.5)
            print("Enemy Health: " + str(enemy.health))
        moveNum += 1   

        if enemy.health <= 0:
            if roundNum == 1:
                xpGained = 100
            else:
                xpGained = random.randint(lvlNum, lvlNum * 100)
            print("You killed the enemy!")
            print("\nYou gained " + str(xpGained) + "xp")
            xpNeeded -= xpGained
            if xpNeeded <= 0:
                print("You leveled up!")
                time.sleep(2)
                levelUp()
            return
        
        elif move == "b":
            c = random.randint(1, 100);
            if c < player.dfc:
                block = True
            else:
                block = False
            turn = "e"
            
        
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
     

    
    battleSequence()

def startRound():
    global player
    global enemy
    global turn
    player = Player()
    enemy = Enemy()
    battleSequence()
startRound()


