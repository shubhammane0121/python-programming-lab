#shubham mane
#factorial.py
#38
#M
#11810247
n=int(input("enter a no.:"))
f=1
if n<0:
      print("enter a positive no.:")
elif n==0 or n==1:
      print("1")
else:
      while n>1:
              f=f*n
              n=n-1
      print(f)






