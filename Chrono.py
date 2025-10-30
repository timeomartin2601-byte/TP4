'''
class score
Braz Arno, Martin Timeo
24/10/25
'''
import time as time
from ast import literal_eval

class lechrono:
    def __init__(self):
        ''' Initialisation de l'objet chronomètre et de ses variables '''
        self.__start_time=0

        self.__historique_chrono=list()
        self.__meilleurs_chrono=list()
        # self.__ligne1=''
        # self.__ligne2=''
        self.__donnée_str=''
        self.__donnée_list=list()

    def start_time(self):
        ''' Démarre le chronomètre à l'appel de la fonction '''
        self.__start_time = time.perf_counter()

    def stop_time(self):
        ''' Stop le chronomètre à l'appel de la fonction '''
        self.__end_time = time.perf_counter()

    def le_chrono(self):
        ''' Renvoie la valeur du chronomètre à l'appel de la fonction '''
        return round(time.perf_counter() - self.__start_time,2)

    def historique_chrono1(self,difficulté):
        ''' Ajoute à l'historique des chrono le dernier chrono réalisé '''
        if len(self.__historique_chrono[difficulté-1]) == 3 :
            del self.__historique_chrono[difficulté-1][0]
        self.__historique_chrono[difficulté-1].append(self.le_chrono())
        return self.__historique_chrono
        
    def classement_chrono1(self,difficulté):
        ''' Renvoie les 4 meilleurs chrono '''
        self.__meilleurs_chrono[difficulté-1].append(self.le_chrono())
        self.__meilleurs_chrono[difficulté-1].sort()
        if len(self.__meilleurs_chrono[difficulté-1]) >= 4 :
            del self.__meilleurs_chrono[difficulté-1][-1]
        return self.__meilleurs_chrono

    def recup_donnée(self):
        ''' Récupère les données des chronomètres enregistrées dans Data '''
        self.__donnée_str = open("data.txt", "r")
        self.__donnée_list=literal_eval("".join(list(self.__donnée_str)))
        self.__historique_chrono=self.__donnée_list[2]
        self.__meilleurs_chrono=self.__donnée_list[3]
        self.__donnée_str.close()

    def memorisation(self):
        ''' Enregistre dans Data le nouveau chronon '''
        donnée_str = open("data.txt", "w")
        donnée_str.write( str([self.__donnée_list[0],self.__donnée_list[1],self.__historique_chrono,self.__meilleurs_chrono]))
        donnée_str.close()
