from sys import stdin, stdout
class Pile:
      
    def __init__(self):
        self.pile = []
				
    def Empiler(self, element):
        return self.pile.append(element)
 
    def Depiler(self):
        try:
            return self.pile.pop()
        except Exception as e:
            print( "Error:", e)
 
    def PileVide(self):
        if self.pile == []:
            return True
        else:
            return False

n =  int(input())


zoo  =  Pile()
for elem in range(n):
    a = input().strip()
    zoo.Empiler(a)

op=0
pile_temp = Pile()
temp =[]

while not zoo.PileVide():
    a = zoo.Depiler()
    if a =='O':
        for elem in temp:
            pile_temp.Empiler('O')
        pile_temp.Empiler('Z')
        op+=1
        temp =[]
    else:
        temp.append(a)
    
    while not pile_temp.PileVide():
        a = pile_temp.Depiler()
        zoo.Empiler(a)
        
print(op)
