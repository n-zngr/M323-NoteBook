# Beispiel: Pure Functions
# Score-Verwaltung für ein Spiel.
# 

currentUser = 0
users = [{"name" : "Holger", "score" : 30, "tries" : 1},
         {"name" : "Verena", "score" : 110, "tries" : 4},
         {"name" : "Peter", "score" : 80, "tries" :3}]
         
print()

def updateScore(newScore):
    users[currentUser]["score"] += newScore

def returnUsers():
    return users

def updateTries():
    users[currentUser]["tries"] += 1

def updateUser(newUser):
    global currentUser
    currentUser = newUser

print(returnUsers())
updateScore(300)
print(returnUsers())
updateUser(2)
updateTries()
print(returnUsers())