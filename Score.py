'''
class score
Braz Arno, Martin Timeo
24/10/25
'''

class lescore:

    def __init__(self):
        self.__score=0

    def augmenter_score(self):
        self.__score += 10 

    def le_score(self):
        return self.__score

    def historique_score(self,historique,difficulté):
        if len(historique[difficulté-1]) == 3 :
            del historique[difficulté-1][0]
        historique[difficulté-1].append(self.__score)
        return historique
        
    def classement_score(self,classement,difficulté):
        if len(classement[difficulté-1]) == 3 :
            del classement[difficulté-1][0]
        classement[difficulté-1].append(self.__score)
        classement[difficulté-1].sort()
        return classement

