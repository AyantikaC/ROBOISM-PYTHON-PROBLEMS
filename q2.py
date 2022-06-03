num=input("enter your credit card number")
l=len(num)
for i in range(0,l-4):
   print("*",end="")
print(num[-4:],end="")
   
