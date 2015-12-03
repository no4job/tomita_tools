import itertools

__author__ = 'mdu'
from functools import reduce
def gaus(b,n,m):
    if n > m:
        _n=m
    else:
        _n=n
    r=n
    for i in range(_n):
        if b[i][i]==0:  # swap with row with non zero base element
            for k in range(i+1,n):
                if b[k][i]!=0:
                    b[i][i],b[k][i]=b[k][i],b[i][i]
                    break
            else:
                r-=1
                if sum(map(abs,b[i][i:m])) == 0 and b[i][m] != 0:  # check for incompatible equation
                    print("NO")
                    return None
        if b[i][i]!=0:# continue with non zero base element
            for k in range(i+1,n):
                c=-1*b[k][i]/b[i][i]
                bm=map(lambda x : x*c,b[i])
                b[k]=list(map(sum,zip(bm,b[k])))
                b[k][0:i]=[0] * i  # remove non zero calculation artifacts
                if sum(map(abs,b[k][i:m])) == 0 and b[k][m] != 0:  # check for incompatible equation
                    print("NO")
                    exit(0)
    if r < m:
        print("INF")
        return None
    x= [None]*m
    for i in reversed(range(_n)):
        if i==_n-1:
            x[i]= b[i][i+1]/b[i][i]
        else:
            x[i]= (b[i][m]-sum(map(lambda y:y[0]*y[1],zip(x[i+1:m],b[i][i+1:m]) )))/b[i][i]
    #print ("YES")
    #print (*x)
    #exit(0)
    return x

def scalar_mult(x,y):
    xy_pair=zip(x,y)
    result = reduce(lambda res, pair: res + pair[0]*pair[1], xy_pair, 0)
    return result
def transp(x):
    res=[]
    for i in range(len(x[0])):
        col=list(map(lambda y: y[i],x))
        res.append(col)
    return res
"""
#i=999999
cnt=0
cnt7=0
cnt71=0
cnt48plus=0
cnt7minus=0
#max_num=999999
#min_num=99999
#dig_sum=47

#max_num=999999
#min_num=0
#dig_sum_7=7
#dig_sum=47

#max_num=99
#min_num=0
#dig_sum_7=2
#dig_sum=16
max_num=999999
min_num=100000
dig_sum_7=7
dig_sum=47


i=max_num
while i >= min_num:
    numbers=[int(j) for j in str(i)]
    s=sum(numbers)
    if s <= dig_sum_7:
        cnt7minus+=1
    if s <= dig_sum:
        cnt+=1
        #print (i)
    else:
        cnt48plus+=1
        #print (i)
        if 7 in numbers:
            cnt7+=1
            #print (i)
    i-=1
#print (cnt,cnt7,cnt71,cnt7minus,cnt48plus)
print (cnt,cnt7minus,cnt48plus)
exit (0)
"""
"""
#positions=list(range(1,41))
cnt_pair=0
cnt_sep=0
pair_flag=0
positions=list(range(1,43))
cmbs=itertools.combinations(positions, 7)
for cmb in cmbs:
    for i in range(len(cmb)-1):
        if cmb[i]+1==cmb[i+1]:
           pair_flag=1
    if pair_flag==1:
        cnt_pair+=1
    else:
        cnt_sep+=1
    pair_flag=0
#print(cmbs)
print(cnt_pair,cnt_sep)
exit (0)
"""
n,m=([int(i) for i in input().split()])
#print(n,m)
_m=m+1
b=[]
for i in range(n):
    b.append([int(i) for i in input().split()])

bt=transp(b)
ee=[]
for i in range(_m):
    e=[]
    for j in range(_m):
        e+=[scalar_mult(bt[i],bt[j])]
    ee.append(e)
x=gaus(ee,m,m)
print (*x)