#global

def kali(a, b):
    c = a*b
    return c #mengembalikan nilai ke baris pemanggil

def tulis(s):
    print(s)


#memanggil fungsi kali
r = kali(10,5)
print(r)


#memanggil fungsi tulis
tulis('pemrograman python dan pyqt')

tulis(r)

#menampilkan nama modul
print(__name__)
