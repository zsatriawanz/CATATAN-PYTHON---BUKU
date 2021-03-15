#gabung
try:
    f = open('contoh.txt','r')
    lines = f.readlines()
    for line in lines:
        print(line, end=' ')
except:
    print('Errro : file tidak ditemukan')
finally:
    if f: f.close()