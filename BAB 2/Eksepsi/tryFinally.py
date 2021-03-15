#menggunakan try..finnaly

#menuliskan data ke dlm file
try:
    f = open('contoh.txt','w')
    f.write('Python\n')
    f.write('Java\n')
    f.write('PHP')
finally:
    f.close()


#membaca ari file
try:
    f = open('contoh.txt','r')
    lines = f.readlines()
    for line in lines:
        print(line, end=' ')
finally:
    f.close