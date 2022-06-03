def func1(L,order):
   if order =="asc":
      for i in range(len(L)-1,0,-1):
         for k in range (i):
            if L[k]> L[k+1]:
               L[k],L[k+1]=L[k+1],L[k]
      print(L)
   elif order=="desc":
      for i2 in range(len(L)-1,0,-1):
         for k2 in range(i2):
            if L[k2]<L[k2+1]:
               L[k2],L[k2+1]=L[k2+1],L[k2]
      print(L)
   elif order=="none":
      print(L)
L1=[]
n=int(input("enter the number of values you want to append"))
for i in range(n):
   elem=int(input("enter a value"))
   L1.append(elem)
ord=input("input asc, desc or none")
func1(L1,ord)
