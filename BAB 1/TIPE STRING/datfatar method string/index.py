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

s = "Pemrograman Python"

a = s.index("o")
print(a)

#index akan mengembalikan nilai error jika nilai yang dinputkan tidak ditemukan
#a = s.index("x")
#print(a)

#untuk mencari index dari kanan gunakan
a = s.rindex("o")
print(a)