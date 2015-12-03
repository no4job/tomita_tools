__author__ = 'mdu'
def recursive_gen(_n,n,k,comb):
    for i in range(_n,n):
        comb[len(comb)-k-1]=i
        if k == 0:
            print (*comb)
            #pass
        else:
            recursive_gen(i+1,n,k-1,comb)
    return
k,n=([int(i) for i in input().split()])
#n=0
#k=0
_n=0
if k==0:
    exit(0)
comb=[None]*k
recursive_gen(_n,n,k-1,comb)

