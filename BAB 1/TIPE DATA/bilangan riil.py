#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Satriawan
#
# Created:     22/12/2020
# Copyright:   (c) Satriawan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import decimal
def main():
    pass

if __name__ == '__main__':
    main()


#bilangan riil

a = 1234.5454
print(a*2)

print(type(a))

a = 8.9e-4
print(a)


#tipe data float ke string
a = 123.456
print(a)

#konvensi ke string
b = str(a)
print(type(b))


#konfensi tupe data string ke float
c = float(b)
print(type(c))


#decima.Decimal
saldo =decimal.Decimal('1232423433.2423425435')
i2 = float('22434334.22324242323232323232323')
print(i2)

print(saldo)
print(type(saldo))

