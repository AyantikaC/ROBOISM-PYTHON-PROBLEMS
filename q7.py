n=int(input("enter the number of elements in the array"))
L1=[]
L2=[]
dict={}
for i in range (0,n):
   num=int(input("enter an element"))
   L1.append(num)
for j in L1:
   if j not in L2:
      L2.append(j)
print(L2)
for k in L2:
   count=0
   for m in range(0,len(L1)):
     if L1[m]==k:
      count=count+1
   dict[k]=count
print(dict)
L3=[]
for x in range(0,len(L2)):
   L3.append(dict[L2[x]])
max1=L3[0]
for y in range(1,len(L2)):
   if L3[y]> max1:
      max1=L3[y]
print(max1)

   
   
