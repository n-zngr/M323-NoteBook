# 323 - Beispiel-1: Abstraktion von Werten in Variablen
#

# Die Liste Gewürz speichert verschiedene Gewürze, auf die via Indexierung zugegriffen werden kann:
gewuerz = ["Pfeffer", "Salz", "Anis", "Curry", "Safran"]

# EIne Funktion sabstrahiert un verallgemeinert eine Codesequenz:
# showSpice printet immer die ganze Datenstruktur gewuerz - unabhängig vom Zustand zur Programmierzeit!
# Zusatzfrage: ist das eine pure Function?
def showSpice():
	for i in gewuerz:
		print(i)

# Zugriff auf die einzelnen Gewürze - bei jeder Anpassung der Gewürzliste muss auch dieser Code angepasst werden....
print("Gewürze1:")
print(gewuerz[0])
print(gewuerz[1])

# Neues Gewürz in Liste aufnehmen:
gewuerz.append("Koreander")


print()
print("Gewürze2:") 
showSpice()
