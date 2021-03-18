class Arimatika:
    @staticmethod
    def tambah(a,b):
        return a+b

    @staticmethod
    def kurang(a,b):
        return a-b

    @staticmethod
    def kali(a,b):
        return a*b

    @staticmethod
    def bagi(a,b):
        return a/b

    @staticmethod
    def bagi_int(a,b):
        return a // b

    @staticmethod
    def sisaBagi(a,b):
        return a % b

    @staticmethod
    def pangkat(a,b):
        return a**b

print(Arimatika.tambah(10,2))
print(Arimatika.kurang(10,2))
print(Arimatika.kali(10,2))
print(Arimatika.bagi(10,2))
print(Arimatika.bagi_int(10,2))
print(Arimatika.sisaBagi(10,2))
print(Arimatika.pangkat(10,2))

#membuat objek dari kelas atribu
obj = Arimatika()
#memaggil metode melalui objek
print(obj.tambah(20,6))
print(obj.pangkat(10,5))