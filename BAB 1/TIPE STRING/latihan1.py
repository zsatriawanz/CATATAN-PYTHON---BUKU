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
#menggunakan tanda petik tunggal
s1 = 'PyQt'
print(s1)

#menggunakan tanda petik ganda
s2 = "Python"
print(s2)

#menggunakan tanda petik tunggal atau ganda yang ditulis tiga kali
s3 = '''
    Pemrograman GUI
    dengan Python dan PyQt'''

print(s3)

s4 = """
    Pemrograman GUI
    dengan Python dan PyQt"""
print(s4)





#mengankses string
a = 'PYTHON'
print(a[0]," ",a[1]," ",a[2]," ",a[3]," ",a[4]," ",a[5])
print(a[5]," ",a[4]," ",a[3]," ",a[2]," ",a[1]," ",a[0])
print(a[-6]," ",a[-5]," ",a[-4]," ",a[-3]," ",a[-2]," ",a[-1])


str1 = "satu dan "
str2 = "dan lagi"
print(str1+str2)