#fungsi lambda
maxs = lambda a,b: a if a > b else b

a = maxs(100,200)

print(a)



nama =['beni','BENO','Benu','asep','ISEP','Usep']
print(nama)

#mengurutkan nama
nama.sort()
print(nama)

#mengurutjan dengan lambda
#huruf esar ke kecil
nama.sort(key = lambda element: element.lower())
print(nama)