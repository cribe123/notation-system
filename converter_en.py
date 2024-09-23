from math import pow
a=input('Enter a number... ')
b=int(input('Enter its system... '))
xpow = 0
for i in range(len(a)-1,-1,-1):
    xpow+=int(a[i])*pow(b,i)
print('Number in decimal system:',int(xpow))
