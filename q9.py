L=[]
n=int(input("enter the number of values in List"))
for i in range (0,n):
   a=int(input("enter a value"))
   L.append(a)
l=len(L)
for j in range (l-1,0,-1):
   for i in range(j):
      if L[i]>L[i+1]:
         L[i],L[i+1]=L[i+1],L[i]
print(L)
