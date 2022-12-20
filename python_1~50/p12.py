#11021
num=int(input())
a=[]
b=[]
for i in range(0,num):
  x,y=input().split()
  x=int(x)
  y=int(y)
  a.append(x)
  b.append(y)
for i in range(0,num):
  result=a[i]+b[i]
  print("Case #",end="")
  print(i+1,end="")
  print(": ",end="")
  print(result)