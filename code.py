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
    dfc = 1
    speed = 1

turn = "p"

moves = ["attack", "block"]

moveNum = 1

roundNum = 1

lvlNum = 1

xpNeeded = 100
xpGained = 0

minLvlUp = 1
maxLvlUp = 3

def levelUp():
    global player
    global lvlNum
    global xpNeeded

    print("\033c")
    print("Which stat would you like to increase?")
    x = input("a to increase attack, d to increase defense, s to increase speed, h to increase health \n")
    lvlUpValue = random.randint(minLvlUp, maxLvlUp)
    if x == "a":
        player.attPower += lvlUpValue
        print("Your attack was increased by " + str(lvlUpValue))
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
    if turn == "e":
        x = random.choice(moves)
        if x == "attack":
            print("The enemy attacked you for " + str(enemy.attPower) + "\n")
            player.health -= enemy.attPower
            turn = "p"
            time.sleep(1.5)
            print("Player Health: " + str(player.health) + "\n")

    
    battleSequence()

def startRound():
    global player
    global enemy
    global turn
    player = Player()
    enemy = Enemy()
    battleSequence()
startRound()
