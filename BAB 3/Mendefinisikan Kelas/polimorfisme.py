from abc import ABCMeta, abstractmethod
class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        pass


class Segiempat(DuaDimensi):
	def __init__(self,p,l):
		self.panjang = p
		self.lebar = l
	def luas(self):
		return self.panjang * self.lebar

class Segitiga(DuaDimensi):
	def __init__(self,a, t):
		self.alas = a
		self.tinggi = t
	def luas(self):
		return (self.alas * self.tinggi)/2

class Lingkaran(DuaDimensi):
	def __init__(self, r):
		self.radius = r
	def luas(self):
		import math
		return math.pi*(self.radius ** 2)

#membuat list kosong
mylist = []
#menambhakan objek segiempat ke dalam mylist
mylist.append(Segiempat(10,8))

#menambah objek segitiga kedalam mylist
mylist.append(Segitiga(3,5))
mylist.append(Segitiga(3,7))

#menambah objek lingkaran kedalam mylist
mylist.append(Lingkaran(4))


#menelusuri seluruh element mylist
#kmeudian memanggil metode luas()
#dari setiap objek yang ditelusuri
for obj in mylist:
    if not issubclass(obj.__class__, DuaDimensi):
        raise TypeError('Objek harus turunan dari Dua Dimensi')
    if isinstance(obj, Segiempat):
        print('Luas segiempat = ',end='')
    elif isinstance(obj, Segitiga):
        print('Luas Segitiga = ',end='')
    else :
        print('Luas Lingkaran = ',end='')
    #baris kode dibawah ini akan
    #memberikan hasil uang berbeda, meskipun perinthanya sama
    print(obj.luas())