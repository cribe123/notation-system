from math import pow
a=input('Введите число... ')
b=int(input('Введите его СС цифрой... '))
xpow = 0
for i in range(len(a)-1,-1,-1):
    xpow+=int(a[i])*pow(b,i)
print('Число в десятичной СС:',int(xpow))
