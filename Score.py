'''
class score
Braz Arno, Martin Timeo
24/10/25
'''
from ast import literal_eval

class lescore:
    def __init__(self):
        ''' Initialisation de l'objet score et des ses variables '''
        self.__score=0
        self.__historique_score=list()
        self.__meilleurs_score=list()
        self.__donnée_str=''
        self.__donnée_list=list()

    def augmenter_score(self):
        ''' Accrémente au score du joueur 10 unités à chaque appel de la fonction '''
        self.__score += 10 

    def mort(self):
        ''' Soustrait au score du joueur 50 unités à chaque appel de la fonction '''
        self.__score-=50

    # def score_temps(self,chrono):
    #     ''' Associe le score avec un facteur temps (WIP) '''
    #     self.__score=self.__score

    def le_score(self,chrono):
        ''' 
        Renvoie le score du joueur
        Entrée : chrono - float, chronomètre actuel du joueur
        Sortie : float, le score du joueur tenant compte du chrono du joueur à 2 dixièmes près
        '''
        return round(self.__score-0.5*chrono,2)

    def historique_score(self,difficulté,chrono):
        ''' Ajoute le dernier score et Renvoie l'historique des scores en fonction de la difficulté '''
        if len(self.__historique_score[difficulté-1]) == 3 :
            del self.__historique_score[difficulté-1][0]
        self.__historique_score[difficulté-1].append(round(self.__score-0.5*chrono,2))
        return self.__historique_score
        
    def classement_score(self,difficulté,chrono):
        ''' Ajoute le dernier score et Renvoie les meilleurs scores en fonction de la difficulté '''
        self.__meilleurs_score[difficulté-1].append(round(self.__score-0.5*chrono,2))
        self.__meilleurs_score[difficulté-1].sort()
        if len(self.__meilleurs_score[difficulté-1]) >= 4 :
            del self.__meilleurs_score[difficulté-1][0]
        return self.__meilleurs_score

    def recup_donnée(self):
        ''' Récupère les données de score des précédentes sessions dans Data '''
        self.__donnée_str = open("data.txt", "r")

        self.__donnée_list=literal_eval("".join(list(self.__donnée_str)))
        self.__historique_score=self.__donnée_list[0]
        self.__meilleurs_score=self.__donnée_list[1]
        self.__donnée_str.close()

    def memorisation(self):
        ''' Inscrit dans Data le nouveau score '''
        donnée_str = open("data.txt", "w")
        donnée_str.write(str([self.__historique_score,self.__meilleurs_score,self.__donnée_list[2],self.__donnée_list[3]]))
        donnée_str.close()





