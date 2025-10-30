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
        '''
        augmentation du score par palier de 10, utilisé lors du cassage d'un bloc
        '''
        self.__score += 10 

    def mort(self):
        '''
        diminution du score par palier de -50, utilisé lors de la perte d'une vie
        '''
        self.__score-=50

    def le_score(self,chrono):
        '''
        retoune le score final egal au score - 0.5 fois le chrono
        parametre chrono : float positif
        '''
        return round(self.__score-0.5*chrono,2)

    def historique_score(self,difficulté,chrono):
        '''
        Ajoute le score a une liste de taille 3 et enleve le premier element, La liste est donc utilisé comme une FILE
        parametre : - dificulté : entier compris entre 1 et 3
                    - chrono : float positif
        retourne la liste modifiée
        '''
        if len(self.__historique_score[difficulté-1]) == 3 :
            del self.__historique_score[difficulté-1][0]
        self.__historique_score[difficulté-1].append(round(self.__score-0.5*chrono,2))
        return self.__historique_score
        
    def classement_score(self,difficulté,chrono):
        '''
        Ajoute le score a une liste de taille 3 et la trie, enleve ensuite le plus petit score
        parametre : - dificulté : entier compris entre 1 et 3
                    - chrono : float positif
        retourne la liste modifiée
        '''
        self.__meilleurs_score[difficulté-1].append(round(self.__score-0.5*chrono,2))
        self.__meilleurs_score[difficulté-1].sort()
        if len(self.__meilleurs_score[difficulté-1]) >= 4 :
            del self.__meilleurs_score[difficulté-1][0]
        return self.__meilleurs_score

    def recup_donnée(self):
        '''
        recupere les données du fichier text data.txt qui contient une liste comprenant 4 sous liste.
        corespondance : - 1er sous liste : historique des scores
                        - 2eme sous liste : meilleurs scores
                        - 3eme sous liste : historique des chronos
                        - 4eme sous liste : meilleurs chronos
        Chaque sous liste contient 3 sous liste car 3 difficulté.
        parametre diificulté : entier compris entre 1 et 3
        '''
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





