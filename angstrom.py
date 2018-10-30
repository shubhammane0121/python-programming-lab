def angstrom_no(x):
       s=0
       z=x
       while x>0:
               y=x%10
               s=y**3+s
               x=x//10
       print(s)
       if s==z:
               print("angstrom no")
       else:
               print("not an angstrom no")
x=int(input("enter a no."))
num=angstrom_no(x)
print(num)
