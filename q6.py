def Prime(a,b):
   L1=[]
   for i in range (a,b+1):
      for j in range(2,i):
         if i%j==0:
            isprime= False
            break
         else:
            isprime= True
      if isprime:
         L1.append(i)
   print(L1)
l=int(input("enter the first val"))
m=int(input("enter the second val"))
Prime(l,m)
