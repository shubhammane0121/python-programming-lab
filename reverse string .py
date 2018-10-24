# Shantanu Tale
#Gr-11810363
#roll no- M-64
#Division-M
def strrev(x):
 y='' 
 l=len(x) 
 while l>0: 
  y+=x[l-1]
  l=l-1 
 return y
x=input()
print(strrev(x))
