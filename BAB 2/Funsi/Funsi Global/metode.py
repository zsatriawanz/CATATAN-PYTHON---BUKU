#metode adalah fungsi di dalam class
class Titik(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def pindah(self, x, y):
        self.x = x
        self.y = y
    def cetak(self):
        print('(%d,%d)' % (self.x, self.y))

#membuat objuk dari kelas Tititk
t = Titik()

#memanggil metode cetak
t.cetak()

#memanggil metode pindah()
t.pindah(5,4)

#memanggil cetak setelah dipindah
t.cetak()