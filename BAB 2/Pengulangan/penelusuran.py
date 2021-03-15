#penelusuran

#penelusuran elemen-elemen list
daftar = ['Python','Ruby','PHP']
for i in daftar:
    print(i)

#peneusuran element -eleent string
for kata in 'Python':
    print(kata)

#penelusuran element -element dictionary
kamus = {'satu':'one','dua':'twu','tiga':'three'}
for kunci,nilai in kamus.items():
    print('%s %s'%(kunci,nilai))

#penelususran tupple
t = (10,11,12,13,14,16)
for i in t:
    print(i, end=' ')

#penelusuran set
r = set([10,12,123,423])

for marget in r:
    print(marget)
