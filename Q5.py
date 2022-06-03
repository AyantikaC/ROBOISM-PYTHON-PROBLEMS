def L():
   L1=[]
   for i in range (0,10):
      elem=int(input("enter a number between 1 and 99"))
      L1.append(elem)
   L2=[]
   for j in range(0,100):
      if L1[j] in L2:
         print(L1[j])
         break
      else:
         L2.append(L1[j])
L()
      
      
   
   
