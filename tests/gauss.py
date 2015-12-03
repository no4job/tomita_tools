__author__ = 'mdu'
"""
n,m=([int(i) for i in input().split()])
#print(n,m)

b=[]
for i in range(n):
    b.append([int(i) for i in input().split()])
    print(b)
"""
"""
n=2
m=2
b=[[1,-1,-5],
   [2, 1,-7]
  ]
"""
"""
n=3 # 3 5 4
m=3
b=[[3,2,-5,-1],
   [2, -1,3,13],
   [1, 2,-1,9]
]
"""
"""
n=3 # NO
m=4
b=[[4,-3,2,-1,8],
   [3, -2,1,-3,7],
   [5, -3,1,-8,1]
]
"""
"""
n=4 # INF
m=4
b=[[2,3,-1,1,1],
   [8, 12,-9,8,3],
   [4, 6,3,-2,3],
   [2, 3,9,-7,3]
]
"""
"""
n=1 #
m=1
b=[[0,1]
]
"""
"""
n=3
m=2
b=[[1,2,1],
   [1, 3,2],
   [1, 3,3]
]
"""

n,m=([int(i) for i in input().split()])
#print(n,m)

b=[]
for i in range(n):
    b.append([int(i) for i in input().split()])
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
                exit(0)
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
    exit (0)
x= [None]*m
for i in reversed(range(_n)):
    if i==_n-1:
        x[i]= b[i][i+1]/b[i][i]
    else:
        x[i]= (b[i][m]-sum(map(lambda y:y[0]*y[1],zip(x[i+1:m],b[i][i+1:m]) )))/b[i][i]
print ("YES")
print (*x)
exit(0)