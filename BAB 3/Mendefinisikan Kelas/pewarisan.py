#membuat kelas turunan dari kelas list
class StringList(list):
    def __init__(self):
        self.data = []
    def __repr__(self):
        return str(self.data)
    #override metode append()
    def append(self, objek):
        if not isinstance(objek, str):
            raise TypeError('Objek harus bertipe string')
        self.data.append(objek)
    #override metode insert()
    def insert(self, indeks, objek):
        if indeks >= len(self.data) or indeks < -len(self.data):
                raise IndexError('Indexs di luar rentang')
        if not isinstance(objek, str):
                raise TypeError('Objek harus bertipe string')
        self.data.insert(indeks, objek)


#mebuat objek dari kelas StringList
slist = StringList()

#menambah data menggunakan metofde append
slist.append('Python')
slist.append('Ruby')
slist.append('PHP')


#menampilkan isi objek slist
print(slist)



#menmabha data menggunakn insert()
slist.insert(2, 'Perl')
slist.insert(-3, 'Java')


#menampilkan isi objek slist
print(slist)


