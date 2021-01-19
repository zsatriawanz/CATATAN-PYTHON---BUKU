#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Satriawan
#
# Created:     24/12/2020
# Copyright:   (c) Satriawan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#mengembalikan objek dari kelas bytes yang mempresentasikan string menggunakan encoding standar
s = "Python"
a = s.encode(encoding='utf-8',errors='strict')
print(a)