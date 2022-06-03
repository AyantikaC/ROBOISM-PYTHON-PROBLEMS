str=input("enter a string")
sum=0
for i in str:
   if i in ("1234567890"):
      sum=sum+int(i)
print(sum)
