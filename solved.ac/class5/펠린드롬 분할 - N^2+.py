s=' '+input()
n=len(s)
d=[0]*n
p=[0]*n
for i in range(n):
    d[i]=i
    for j in range(i+1):
        if s[j]==s[i]and(i-j<=1or p[j+1]):p[j]=1;d[i]=min(d[i],d[j-1]+1)
        else:p[j]=0
print(d[i])