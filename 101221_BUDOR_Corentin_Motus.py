
from random import random
from colorama import init
init()
from colorama import Fore, Back, Style
#print(Fore.WHITE + 'texte en blanc',end="")
#print(Back.BLUE + 'and with a blue background')
#print(Back.RED + 'and with a red background')
#print(Back.YELLOW +  'and with a yellow background')
#print('back to normal now')
#input()

Mot_Joueur =""
Mot = ""
Proposition = ""
lettre =""

Reponse1 = ["CASTOR"]
Reponse2 = ["CINEMA"]
Reponse3 = ["CYPRES"]
Reponse4 = ["CITRON"]
Reponse5 = ["JOCKEY"]
Reponse6 = ["JOYAUX"]
Reponse7 = ["HOCKEY"]
Reponse8 = ["BIJOUX"]
Reponse9 = ["CYBORG"]
Reponse10 =["JUDOKA"]

Mot_a_Trouver = [ Reponse1, Reponse2, Reponse3, Reponse4, Reponse5, Reponse6, Reponse7, Reponse8, Reponse9, Reponse10]

if (Mot_a_Trouver== 1) :
    Mot = Reponse1
if (Mot_a_Trouver == 2) :
    Mot = Reponse2
if (Mot_a_Trouver == 3) :
    Mot = Reponse3
if (Mot_a_Trouver == 4) :
    Mot = Reponse4
if (Mot_a_Trouver == 5) :
    Mot = Reponse5 
if (Mot_a_Trouver == 6) :
    Mot = Reponse6
if (Mot_a_Trouver == 7) :
    Mot = Reponse7
if (Mot_a_Trouver == 8) :
    Mot = Reponse8
if (Mot_a_Trouver == 9) :
    Mot = Reponse9
if (Mot_a_Trouver == 10) :
    Mot = Reponse10 

#Mot_a_Trouver=random.randint(1, 10) 

#--Affichage lettre
for i in range (0,10) :
    if Mot_Joueur == Mot_a_Trouver :
        print(Back.RED + Mot_Joueur,end="")
    else :
        print(Back.BLUE + Mot_Joueur)

#--Victoire/Defaite
for i in range (1,8) :
    int(input("A quel mot pense tu ?"))
    if Mot_Joueur == Mot_a_Trouver:
        print ("Bravo, vous avez gagnez")
    else:
        if Proposition > 8 :
            print ("Dommage vous avez perdu")


while Mot_a_Trouver != True:
    print ("nombre de choix restant :",Proposition)
    Mot_Joueur = input(" A quel mot pense tu ?")
    for i in range (len(Mot_a_Trouver)):
        if Mot_Joueur[i] == Mot_a_Trouver[i]:
            print(Back.RED + Mot_Joueur, end="")
        else :
            print(Back.BLUE + Mot_Joueur)
            


