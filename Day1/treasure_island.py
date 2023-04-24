print("================ WELCOME TO TREASURE ISLAND ================")

startingPicture = """
                           _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           '.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
"""
print(startingPicture)

#function for asking next move
def leftOrRight():
   return input('Do you want to go left or right ??')

# showing gameover message
def gameOver():
    print('GAME OVER')

#shows you find a treasure
def treasureFound():
    print('You find the treasure')

#app
print('Your mission is to find the treasure')

answer = leftOrRight()

if(answer == 'right'):
    print('You are in the Monster ROOM ')
    answer = leftOrRight()

    if(answer == 'right'):
        gameOver()
    else :
            if(answer == 'left'):
                treasureFound()
            else :
                print('You have been killed by the Monters')
                gameOver()  
else:
    if(answer == 'left'):
        print('You are in the Snake ROOM ')
        answer = leftOrRight()
        if(answer == 'left'):
            gameOver()
            print('You have been killed by Snakes')

        else: 
            if(answer == 'right'):
                treasureFound()
            else : 
                gameOver()
    else :
        gameOver()
print('================ End for game ===============')

##Runtime of code ##
print('The runtime of the code is')