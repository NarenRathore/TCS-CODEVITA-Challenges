import re,sys
N=int(input())
l3=[]
l4=[]
if N in range(1,1001):
    for i in range (N):
        P=input()
        S=input()
        l1=list(P)
        l2=list(S)
        if len(P)==26 and len(S) in range(1,101) and re.match("^[a-z]*$",P) and re.match("^[a-z]*$",S):
            for j in range(len(S)):
                for j in l1:
                    if j in l2:
                        l3.append(j)
                        
                        l2.remove(j)
                        
                        break
               
            l4.append("".join(l3))
            del l3[:]
            
        else:
            sys.exit()
    for i in l4:
                print(i)
            del l4[:]
else:
    sys.exit()
