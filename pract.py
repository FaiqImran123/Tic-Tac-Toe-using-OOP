class Board():
    def __init__(self,):
        self.li =["_"]*9

    def display(self):
        print(f"{self.li[0]}|{self.li[1]}|{self.li[2]}")
        print(f"{self.li[3]}|{self.li[4]}|{self.li[5]}")
        print(f"{self.li[6]}|{self.li[7]}|{self.li[8]}")
    def update(self, location, ply):
        if (location<10 and location>0) and  (self.li[location-1]=="_"):
            self.li[location-1]=ply
            stat =self.check(ply)
            if stat!="continue":
                return f"{ply} {stat}"
            else:
                return stat
        else:
            return "Invalid Location"
        
    def check(self,ply):
        if self.li[0]==ply and self.li[1]==ply and self.li[2]==ply:
            return "win"
        elif self.li[2]==ply and self.li[4]==ply and self.li[6]==ply:
            return "win"

        elif self.li[0]==ply and self.li[3]==ply and self.li[6]==ply:
            return "win"
        elif self.li[0]==ply and self.li[4]==ply and self.li[8]==ply:
            return "win"
        elif self.li[6]==ply and self.li[7]==ply and self.li[8]==ply:
            return "win"
        elif self.li[6]==ply and self.li[4]==ply and self.li[2]==ply:
            return "win"
        elif self.li[8]==ply and self.li[5]==ply and self.li[2]==ply:
            return "win"
        else:
            return "continue"



def main():
    

    ans ="yes"
    while ans=="yes":
        i =1
        b =Board()
        while i<10:
            if i==1:
                b.display()
        

            if i%2==0:
                #O for player 2
            
                player_2=int(input(("Enter Input(Ply 2):  ")))
                
                ply ="O"
                stat =b.update(player_2, ply)
                if stat=="Invalid Location":
                    print("Invalid Location")
                    i =i-1
                elif stat!="continue":
                    b.display()
                    print(stat)
                    break
                else:
                    b.display()
                

            else:
                #X for player 1
                player_1 =int(input("Enter Location(Ply 1):  "))
                ply ="X"
                stat =b.update(player_1, ply)
                if stat=="Invalid Location":
                    print("Invalid Location")
                    i =i-1
                elif stat!="continue":
                    b.display()
                    print(stat)
                    break
                else:
                    b.display()
        

            i =i+1
            if i==10:
                print("Tie")
        ans =input("Want to Play Again(yes or no): ")




main()