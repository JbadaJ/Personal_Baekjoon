#2588
a=int(input())
b=int(input())
print(a*(b%10)) #3 O
print(a*((b//10)%10)) #4 O
print(a*(b//100)) #5 O
print(a*b) #마지막줄 O