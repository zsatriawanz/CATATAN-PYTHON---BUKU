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

def main():
    pass

if __name__ == '__main__':
    main()


#convensi bilangan bulat ke string
a = 12345
print(type(a))
#mengkonvensi a ke tipe dta sring
b = str(a)

print(b + " suda di rubah menjadi string")

print(type(str(a)))
#convensi string ke integer
a = '12345'
print(type(a))
#convensi a ke int
b = int(a)
print(b)

print(type(b))


#bilangan biner
a = 0b1001
print(a)
#bilangan oktal
b = 0o23
print(b)
#bilangan hexadesimal
c= 0x2f
print(c)

#tipe boolean
a=(int(True))
b=(int(False))
print(a,b)


#semua tipe numerik berisfat immutable
a = 18
print(id(a))

a += 1

print(id(a))