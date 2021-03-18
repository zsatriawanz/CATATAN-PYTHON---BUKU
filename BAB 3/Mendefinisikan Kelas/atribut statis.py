class PersegiPanjang:
    # atribut statis
    counter = 0
    def __init__(self, p ,l):
        #menaikkan nilai atribut statis
        PersegiPanjang.counter +=1
        #atribut-atribut non-statis
        self.panjang = p
        self.lebar = l
    def ubahPanjang(self, p):
        self.panjang = p
    def ubahLebar(self, l):
        self.lebar = l
    def hitungLuas(self):
        return self.panjang * self.lebar
    def hitungKeliling(self):
        return 2* (self.panjang+self.lebar)
    def cetakLuas(self):
        print ('Luas persegi panjang = %.2f' %  self.hitungLuas())
    def cetakKeliling(self):
        print ('Keliling persegi panjang = %.2f' % self.hitungKeliling())


#obj1 = PersegiPanjang(10, 8)
#obj1.cetakKeliling()

#membuat tiga objek dari kelas persegi panjang
obj4 = PersegiPanjang(20,15)
obj2 = PersegiPanjang(10,8)
obj3 = PersegiPanjang(7,5)

#memanggil atribut counter melalui referensi/objek

print(obj2.counter)
print(obj3.counter)
print(obj4.counter)
