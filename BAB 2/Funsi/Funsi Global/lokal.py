def cetakbonus(daftar=[]):
    def hitungbonus(gaji):
        if gaji < 5000000:
            bonus = 0.05 * gaji
        elif 5000000 <= gaji < 7500000:
            bonus = 0.10 * gaji
        else:
            bonus = 0.15*gaji
        return bonus
    for nama, gaji in daftar:
        b = hitungbonus(gaji)
        print('%s\t%d\t%.2f' %(nama,gaji,b))


data = [
    ('Agus',4000000),
    ('Andi',6000000),
    ('Beno',8000000)]

#memanggil fungsi cetakbonus()
cetakbonus(data)