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

        self.__historique_chrono=list()
        self.__meilleurs_chrono=list()
        # self.__ligne1=''
        # self.__ligne2=''
        self.__donnée_str=''
        self.__donnée_list=list()

    def start_time(self):
        self.__start_time = time.perf_counter()

    def stop_time(self):
        self.__end_time = time.perf_counter()

    def le_chrono(self):
        return round(time.perf_counter() - self.__start_time,2)

    def historique_chrono1(self,difficulté):
        if len(self.__historique_chrono[difficulté-1]) == 3 :
            del self.__historique_chrono[difficulté-1][0]
        self.__historique_chrono[difficulté-1].append(self.le_chrono())
        return self.__historique_chrono
        
    def classement_chrono1(self,difficulté):
        self.__meilleurs_chrono[difficulté-1].append(self.le_chrono())
        self.__meilleurs_chrono[difficulté-1].sort()
        if len(self.__meilleurs_chrono[difficulté-1]) >= 4 :
            del self.__meilleurs_chrono[difficulté-1][-1]
        return self.__meilleurs_chrono

    def recup_donnée(self):
        self.__donnée_str = open("data.txt", "r")
        self.__donnée_list=literal_eval("".join(list(self.__donnée_str)))
        self.__historique_chrono=self.__donnée_list[2]
        self.__meilleurs_chrono=self.__donnée_list[3]
        self.__donnée_str.close()

    def memorisation(self):
        donnée_str = open("data.txt", "w")
        donnée_str.write( str([self.__donnée_list[0],self.__donnée_list[1],self.__historique_chrono,self.__meilleurs_chrono]))
        donnée_str.close()
