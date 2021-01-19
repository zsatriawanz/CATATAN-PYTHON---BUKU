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



#mengecek perbandingan == dan is
s1 = 'Pemrograman Python'
s2 = 'Pemrograman ' + 'Python'

print(s1 == s2)
print(s1 is s2)
print(id(s1))
print(id(s2))


s3 = 'python'
s4 = 'PYTHON'

print(s3 == s4)
print(s3 != s4 )
print(s3 < s4)
print(s3 <= s4)
print(s3 > s4)
print(s3 >= s4)


