'''
class score
Braz Arno, Martin Timeo
24/10/25
'''
import time as time
from ast import literal_eval

class lechrono:
    def __init__(self):

        self.__start_time=0
        self.__end_time=0
        self.__chrono=0
        self.__historique_chrono=list()
        self.__meilleurs_chrono=list()
        self.__donnée_str=''
        self.__donnée_list=list()

    def start_time(self):
        '''
        attribue a self.__start_time l'heure de debut de partie
        '''
        self.__start_time = time.perf_counter()

    def time(self):
        '''
        attribue a self.__end_time l'heure actuelle
        '''
        self.__end_time = time.perf_counter()

    def le_chrono(self):
        '''
        renvoie le chrono
        '''
        self.__chrono = round(self.__end_time - self.__start_time,2)
        return self.__chrono

    def historique_chrono1(self,difficulté):
        '''
        Ajoute le chrono a une liste de taille 3 et enleve le premier element, La liste est donc utilisé comme une FILE
        parametre : - dificulté : entier compris entre 1 et 3f
        retourne la liste modifiée
        '''
        if len(self.__historique_chrono[difficulté-1]) == 3 :
            del self.__historique_chrono[difficulté-1][0]
        self.__historique_chrono[difficulté-1].append(self.le_chrono())
        return self.__historique_chrono
        
    def classement_chrono1(self,difficulté):
        '''
        Ajoute le score a une liste de taille 3 et la trie, enleve ensuite le plus petit score
        parametre : - dificulté : entier compris entre 1 et 3
        retourne la liste modifiée
        '''
        self.__meilleurs_chrono[difficulté-1].append(self.le_chrono())
        self.__meilleurs_chrono[difficulté-1].sort()
        if len(self.__meilleurs_chrono[difficulté-1]) >= 4 :
            del self.__meilleurs_chrono[difficulté-1][-1]
        return self.__meilleurs_chrono

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
        self.__historique_chrono=self.__donnée_list[2]
        self.__meilleurs_chrono=self.__donnée_list[3]
        self.__donnée_str.close()

    def memorisation(self):
        '''
        modifie le fichier data.txt
        '''
        donnée_str = open("data.txt", "w")
        donnée_str.write( str([self.__donnée_list[0],self.__donnée_list[1],self.__historique_chrono,self.__meilleurs_chrono]))
        donnée_str.close()
