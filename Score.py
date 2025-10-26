'''
class score
Braz Arno, Martin Timeo
24/10/25
'''
from ast import literal_eval


class lescore:

    def __init__(self):
        self.__score=0
        self.__historique_score=list()
        self.__meilleurs_score=list()
        self.__donnée_str=''
        self.__donnée_list=list()

    def augmenter_score(self):
        self.__score += 10 

    def le_score(self):
        return self.__score

    def historique_score(self,difficulté):
        if len(self.__historique_score[difficulté-1]) == 3 :
            del self.__historique_score[difficulté-1][0]
        self.__historique_score[difficulté-1].append(self.__score)
        return self.__historique_score
        
    def classement_score(self,difficulté):
        self.__meilleurs_score[difficulté-1].append(self.__score)
        self.__meilleurs_score[difficulté-1].sort()
        if len(self.__meilleurs_score[difficulté-1]) >= 4 :
            del self.__meilleurs_score[difficulté-1][0]
        return self.__meilleurs_score

    def recup_donnée(self):
        self.__donnée_str = open("data.txt", "r")

        self.__donnée_list=literal_eval("".join(list(self.__donnée_str)))
        self.__historique_score=self.__donnée_list[0]
        self.__meilleurs_score=self.__donnée_list[1]
        self.__donnée_str.close()

    def memorisation(self):
        donnée_str = open("data.txt", "w")
        donnée_str.write(str([self.__historique_score,self.__meilleurs_score,self.__donnée_list[2],self.__donnée_list[3]]))
        donnée_str.close()





