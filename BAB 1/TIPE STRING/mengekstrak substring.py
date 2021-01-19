#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Satriawan
#
# Created:     23/12/2020
# Copyright:   (c) Satriawan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

s4 = "PYTHON adalah sebuah bahasa pemrograman"
print(s4[0:6])
print(s4[3:9])
print(len(s4))

#menggunakan index negatif untuk mengambil indek substring
s = "belajar pemrograman python"
print(s[-5:len(s)])


print(s[:])
print(s[:15])
print(s[:11:2])