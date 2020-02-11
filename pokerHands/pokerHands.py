import sys

class PokerHand:
    # tipo de mano (alta,pareja, doblePar, trio, escalera, color, full, poker, escalera color)
    # ranked
    # su numero indica el tipo de mano que tiene, empezando en 0 para carta alta, pareja 1,etc
    # bestHand
    

    def sortHand(self,hand):
        ranks = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
        sorted_cards = sorted(((ranks[v[0]], v[1]) for v in hand),
            key=lambda x: (x[0], x[1]))
        values, suits = zip(*sorted_cards)
        return values, suits

    def __init__(self, hand):
        self.bestHand = 0
        self.ranked = [None] * 9
        
        self.values, self.suits = self.sortHand(hand)
        self.calculateHand()

    def getRanked(self):
        return self.ranked

    def getValues(self):
        return self.values

    def getSuits(self):
        return self.suits

    def calculateHand(self):
        #carta alta
        self.ranked[0] = self.values[4]

        posibleThree = False
        posibleFour = False
        flush = 0
        posibleStraight = True
        for i,x in enumerate(self.values[:-1]):
            if x == self.values[i + 1]:
                if posibleFour:
                    #poker
                    self.ranked[7] = x
                    self.bestHand = 7
                    posibleFour = False
                elif posibleThree:
                    if self.ranked[1] != None and self.ranked[1] != x:
                        #full 2 + 3
                        self.ranked[6] = x, self.ranked[1]
                        self.bestHand = 6
                    # trio
                    self.ranked[3] = x
                    posibleThree = False
                    posibleFour = True
                    if self.bestHand < 3:
                        self.bestHand = 3
                else:
                    if self.ranked[3] != None:
                        #full 3 + 2 pero muestra formato para a la izquierda trio
                        self.ranked[6] = self.ranked[3], x
                        self.bestHand = 6
                    elif self.ranked[1] != None:
                        #doble pareja
                        self.ranked[2] = x, self.ranked[1]
                        self.bestHand = 2
                    else:
                        #pareja
                        self.ranked[1] = x
                        self.bestHand = 1
                    posibleThree = True
            else:
                posibleThree = False
                posibleFour = False
            
            # para el color
            if self.suits[i] == self.suits[i + 1]:
                flush += 1

            # para la escalera
            if posibleStraight and x != self.values[i + 1] - 1:
                posibleStraight = False

        #comprobar si es color y asignarlo
        if flush == 4:
            self.ranked[5] = self.ranked[0]
            if self.bestHand < 5:
                self.bestHand = 5

        #comprobar si es escalera
        if posibleStraight:
            #comprobar si es escalera de color
            if self.ranked[5] != None:
                self.ranked[8] = self.values[-1]
                self.bestHand = 8
            self.ranked[4] = self.values[-1]
            if self.bestHand < 4:
                self.bestHand = 4

    # > 0 gano yo, 0 empate, < 0 gana otherHand
    def compareHand(self,otherHand):
        if self.bestHand == otherHand.bestHand:
            if self.bestHand == 1 or self.bestHand == 2 or self.bestHand == 3 or self.bestHand == 6 or self.bestHand == 7:
                #pareja, doble pareja, trio, poker
                return self.compareSameHand(otherHand)
            elif self.bestHand == 2:
                #doble pareja
                return self.compareSameHand(otherHand)
            elif self.bestHand == 4 or self.bestHand == 8:
                #escalera, escalera color
                return self.ranked[self.bestHand] - otherHand.ranked[otherHand.bestHand]
            else:
                #carta alta, color
                return self.hightesCardCompare(self.values, otherHand.values) 
        elif self.bestHand > otherHand.bestHand:
            return 1
        else:
            return -1
    
    def hightesCardCompare(self,conjunt,otherConjunt):
        i = len(conjunt) - 1
        result = conjunt[i] - otherConjunt[i]
        while result == 0 and i > 0:
            i -= 1
            result = conjunt[i] - otherConjunt[i]
        return result

    def removedCards(self, otherHand):
        black = set()
        white = set()
        if self.bestHand == 1:
            black.add(self.ranked[self.bestHand])
            white.add(otherHand.ranked[otherHand.bestHand])

        blackList = sorted(list(set(self.values) - black))
        whiteList = sorted(list(set(otherHand.values) - white))
        return blackList, whiteList

    def compareSameHand(self,otherHand):
        if self.ranked[self.bestHand] == otherHand.ranked[otherHand.bestHand]:
            listBlack, listWhite = self.removedCards(otherHand)
            return self.hightesCardCompare(listBlack, listWhite)
        elif self.ranked[self.bestHand] > otherHand.ranked[otherHand.bestHand]:
            return 1
        else:
            return -1

if __name__ == '__main__':
    while True:
        try:
            line = None
            line = input()
        except:
            pass
        
        if line is None: break
        
        line = line.strip()
        if len(line) == 0: break
        
        blackCards = list()
        whiteCards = list()
        
        for i, x in enumerate(line.split()):
            if i < 5:
                blackCards.append(x)
            else:
                whiteCards.append(x)

        blackHand = PokerHand(blackCards)
        whiteHand = PokerHand(whiteCards)

        bestHand = blackHand.compareHand(whiteHand)
        if bestHand > 0:
            print("Black wins.")
        elif bestHand < 0:
            print("White wins.")
        else:
            print("Tie.")