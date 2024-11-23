# Beispiel: Pure Functions Lösungsvorschlag
# Verwaltung einer Scoretabelle mit einer Liste aus Dictionaries.

users = [{"name" : "Holger", "score" : 30, "tries" : 1},            # Datenstruktur users ist global, aber zentrale Datenstruktur
         {"name" : "Verena", "score" : 110, "tries" : 4},           # Es ist zu beachten, dass hier die Namen als Id's nicht eindeutig sind!
         {"name" : "Peter", "score" : 80, "tries" :3}]              # Hier wäre eine numerische Id oder ein anderer eindeutiger Identifier sicher besser!
         


# impure Functions:
def updateScore(usrList, user, newScore):                       # Verändert users, da Übergabe call by Reference
    # update Score
    usrList[user]["score"] += newScore
    return usrList

def updateTries(usrList, user):                                 # Verändert users, da Übergabe call by Reference
    #increment Tries
    usrList[user]["tries"] += 1


# pure Functions:
def getUser(usrList, user):                                     # erhält zwar users übergeben via call by reference, verändert die Lieste aber nicht!
    for i in usrList:
        if i["name"] == user:
            return users.index(i) 

def getScore(usrList, name):                                    # erhält zwar users übergeben via call by reference, verändert die Lieste aber nicht!
    for i in usrList:
        if i["name"] == name:
            return(name, i["score"])  
  
def getTries(usrList, name):                                    # erhält zwar users übergeben via call by reference, verändert die Lieste aber nicht!
    for i in usrList:
        if i["name"] == name:
            return(name, i["tries"])  

    
print(getScore(users.copy(), "Holger"))
users = updateScore(users.copy(), getUser(users.copy(), "Holger"), 200)
print(getScore(users.copy(), "Holger"))

print(getTries(users.copy(), "Verena"))
updateTries(users, getUser(users.copy(), "Verena"))
print(getTries(users.copy(), "Verena"))


