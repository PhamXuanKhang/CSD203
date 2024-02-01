import math
from Stack import *
class Graph:
    def __init__(self,data):
        self.a = data
    def display(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print(self.a[i][j], end =" ")
            print("")
        print("")
    def depthFirst(self,start, m):
        b = [True]*len(self.a)
        b[start] = False    
        self.depth(start,b, m)
        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.depth(i,b,m)
    def depth(self,start,b, m): # m is the chosen type for print: 0 is no vertex number
        t = self.deg(start)
        if m == 0:
            print(f"{chr(start+65)}", end = " ")
        elif m == 1:
            print(f"{chr(start+65)}({t})", end = " ")
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth(i,b,m)
    def deg(self, x):
        count =0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count
    #----------------------------
    def f1(self,start):
        self.depthFirst(start, 0)
        print("")
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1========
        self.depthFirst(start, 1)


        #---------------------------
        print("")
    
    #----------------------------    
    '''Algorithm for finding an Euler cycle from the vertex X using stack 
//Input: Connected graph G with all vertices having even degrees
//Output: Euler cycle
declare a stack S of characters
declare empty array E (which will contain Euler cycle)
push the vertex X to S
while(S is not empty)
 {r = top element of the stack S 
  if r is isolated then remove it from the stack and put it to E
   else
   select the first vertex Y (by alphabet order), which is adjacent
   to r, push  Y  to  S and remove the edge (r,Y) from the graph   
 }
 the last array E obtained is an Euler cycle of the graph'''
    #-------------------------------------
    def f2(self,start):
        #===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        S = Stack()
        E = []
        F = []
        S.push(start)
        while not S.isEmpty():
            r = S.top
            print(r)
            if self.deg(r) == 0:
                S.pop()
                E.append(r)
            else:
                for i in range(len(self.a)):
                    if self.a[r][i] != 0:
                        F.append(i)
                F.sort()
                Y = F[0]
                S.push(Y)
                self.a[r][Y] = 0
            print(E)
            
          


        #------------------------------
        print("")
        

    # -----------------------------
    def f3(self,start,end):
        
        pass
