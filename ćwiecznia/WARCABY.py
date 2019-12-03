# CTRL+ALT+L -> auto-formatowanie




class Warcaby:
# pole klasowe -> słownik zawierający 8 słowników
    warcaby = {
        8: {1: "_", 2: "o", 3: "_", 4: "o", 5: "_", 6: "o", 7: "_",
            8: "o"},
        7: {1: "o", 2: "_", 3: "o", 4: "_", 5: "o", 6: "_", 7: "o",
            8: "_"},
        6: {1: "_", 2: "o", 3: "_", 4: "o", 5: "_", 6: "o", 7: "_",
            8: "o"},
        5: {1: "_", 2: "_", 3: "_", 4: "_", 5: "_", 6: "_", 7: "_",
            8: "_"},
        4: {1: "_", 2: "_", 3: "_", 4: "_", 5: "_", 6: "_", 7: "_",
            8: "_"},
        3: {1: "x", 2: "_", 3: "x", 4: "_", 5: "x", 6: "_", 7: "x",
            8: "_"},
        2: {1: "_", 2: "x", 3: "_", 4: "x", 5: "_", 6: "x", 7: "_",
            8: "x"},
        1: {1: "x", 2: "_", 3: "x", 4: "_", 5: "x", 6: "_", 7: "x",
            8: "_"}
    }

    # metoda klasowa wypisująca szachownicę
    def printBoard(self):
        # iteracja po sekwencji wierszy
        print("| %1s | %1s | %1s | %1s | %1s | %1s | %1s | %1s | " % ("A","B","C","D","E","F","G","H"))
        for row in self.warcaby.keys():
            #iteracja po polach w wierszu
            for key in self.warcaby[row].keys():
                print("| %1s " % (self.warcaby[row][key]), end = "")
            print("| %1d \n" % (row), end="")
        print()
    def getPoint(self):
        print(self.warcaby[3][3])
    def checkMoveFromTo(self, rowStart, columnStart, rowStop, columnStop,type):
        if(rowStart in self.warcaby.keys() and columnStart in self.warcaby[rowStart].keys()):
            # sprawdzanie poprawności ruchu
            if(type == "x" and rowStop == (rowStart + 1) and (columnStop == (columnStart + 1)) or (columnStop == (columnStart -1))):
                self.movePoint(rowStart, columnStart, rowStop, columnStop,type)
            elif(type == "o" and rowStop == (rowStart - 1) and (columnStop == (columnStart + 1)) or (columnStop == (columnStart  - 1))):
                self.movePoint(rowStart, columnStart, rowStop, columnStop, type)
            else:
                print("błędny ruch")
        else:
            print("błędny adres pionka")

            print("dopuszczalne ruchy")
            print(self.warcaby[row + 1][column + 1])
            print(self.warcaby[row + 1][column - 1])
    def movePoint(self, rowStart, columnStart, rowStop, columnStop,type):
        # przesunięcie pionka na nową pozycję
        self.warcaby[rowStop][columnStop]= type

        # i aktualizacja pustego miejsca pozostałego po pionku
        self.warcaby[rowStart][columnStart] = " "
        self.printBoard()
w1 = Warcaby()
w1.printBoard()
w1.getPoint()
w1.checkMoveFromTo(3,1,4,2,"x")
w1.checkMoveFromTo(4,2,5,1,"x")
w1.checkMoveFromTo(5,1,6,2,"x")