### check the randomness of coins flip on the heaad side

from random import *
class coin:
    a=0
    def __init__(self):
       self.a=randint(0,1)

class dice:
    a=0
    def __init__(self):
        #for i in range(n):
        self.a=randint(1,6)

def check_unit(A , n):
    x=0
    l=[]
    for c in A:
        if c.a==n:
            x+=1
        l.append(c.a)
    print(l)
    return x

x=int(input("Input the Number of coins \nIf no coins needed press 0\n"))
if x > 0:
    c=[coin() for oin in range(0,x)]

    for1=check_unit(c,1)
    print((for1/x)*100)

print("\n\nThe next input is to find the probability of the occurance of a number(1-6) in a dice")
print("give input in the form of (number of dice,number which we want to find")

y,z=int(input("first parameter no of dice\t")),int(input("second parameter which number to be checked\t"))

if y > 0 and (0 < z < 7):
    c=[dice() for obj in range(0,y)]

    forz=check_unit(c,z)
    print((forz/y)*100)
    

