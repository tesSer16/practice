y=input
n=int(y())
a=list(map(int,y().split()))
k=int(y())
f=[-1,1][a[0]>k]
print('T'if any([f*a[i-1]<=f*i*k for i in range(1,n+1)])else'F')
