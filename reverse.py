#reverse string

# Shubham mane
#Gr-11810247
#roll no- M-38
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