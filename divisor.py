T=int(input())
if T in range(1,16):
    for i in range (T):
        N=int(input())
        if N in range(1,1000000000000001):
            for j in range(1,N//2+1):
                if N%j==0:
                    print(j,end=' ')
            print(N)
        
    

        
            
            
