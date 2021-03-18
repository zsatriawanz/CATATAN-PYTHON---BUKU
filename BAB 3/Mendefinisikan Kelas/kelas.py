class PersegiPanjang:
    def __init__(self, p, l):
        #mendefinisikan atrubut
        self.panjang = p
        self.lebar = l
    def ubahPanjang(self, p):
        self.panjang = p
    def ubahLlebar(self, l):
        self.lebar = l
    def hitungLuas(self):
        return self.panjang * self.lebar
    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)
    def cetakLuas(self):
        print('Luas Persegi panjang = %.2f' % self.hitungLuas())
    def cetakKeliling(self):
        print('Keliling persegi panjan = %.2f' % self.hitungKeliling())


#membuat objeck dari kelas Persegi panjang
obj1 = PersegiPanjang(10,8)

#memanggil metode cetak luas
obj1.cetakLuas()

#memanggil metodekeliling
obj1.cetakKeliling()


#membuat objek baru
obj2 = PersegiPanjang(12,45)

obj2.cetakKeliling()
obj2.cetakLuas()