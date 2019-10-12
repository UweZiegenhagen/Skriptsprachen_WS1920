
def berechne_KSt_satz(bundesland):
    if bundesland == "Bayern" or bundesland == "Baden-Württemberg":
        return "8%"
    else:
        return "9%"
    
#print(berechne_KSt_satz("Hessen"))
#print(berechne_KSt_satz("Bayern"))

def berechne_KSt_satz2(bundesland):
    if bundesland[0] == "B" and bundesland[1] == "a":
        return "8%"
    else:
        return "9%"
 
#print(berechne_KSt_satz2("Hessen"))
#print(berechne_KSt_satz2("Bayern"))
#print(berechne_KSt_satz2("Saarland"))

def berechne_KSt_satz3(bundesland):
    if bundesland[:2] == "Ba":
        return "8%"
    else:
        return "9%"
 
print(berechne_KSt_satz3("Hessen"))
print(berechne_KSt_satz3("Bayern"))
print(berechne_KSt_satz3("Brandenburg"))    