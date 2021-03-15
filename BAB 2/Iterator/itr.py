#Objek ieratro
li = [10,20,30,40,50]

#mendapatkan objek iterator dari objek list
itr = li.__iter__()

#mendapatkan eleemt pertama
element = itr.__next__()
print(element)
#mendapatkan element - lemen berikutknya
while element:
    print(element, end=' ')
    try:
        element = itr.__next__()
    except StopIteration as e:
        print()
        break


