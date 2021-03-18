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



obj1 = Segiempat(10,8)
print(obj1.luas())

obj2 = Segitiga(3,5)
print(obj2.luas())


obj3 = Lingkaran(4)
print(obj3.luas())
