#try..except
try:
    a = int(input('Masukkan nilai a :'))
    b = int(input('Masukkan nilai b :'))
    c = a/b
    print('%d / %d = %.2f ' % (a,b,c))
except ZeroDivisionError as e:
    #print('ERROR : terjadi pembagian nol.')
    #pass untuk mengabaikan kesalahan
    pass


