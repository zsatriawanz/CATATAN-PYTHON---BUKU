
#perlu diimpor ke setiap program Pyqt5 karena kita akan menggunakn sys.argv
#di QApplication
import  sys

#mengimpor kelas QApplication, QWidget, QLabel untuk mendefinisikan
#dari dalam modul QtWidgets yang berada dalam PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    #berguna untuk membuat objek (instance) dari kelas QApplication
    #setiap program yang ditulis menggunakan memghgunakan PyQt5
    #harus memiliki QAppication
    a = QApplication(sys.argv)

    #membuat objek dari kelas QWidget
    #berperan sebagai form utama dari program yang kita buat
    form = QWidget()

    #resize() pada kelas QWidget bergunauntuk mengubah ukuran form
    form.resize(500,300)

    #Metode move() pada kelas QWidget (dan kelas kelas lain) berguna
    #untuk menentukan posisi atau koordinat form pada tampilan
    form.move(400,200)

    #Pemangggilan metode resize() dan move() bisa diganti dengan
    #setGeometry(), menjadi
    #form.setGeometry(300,300,200,100)

    #menetukan judul form
    form.setWindowTitle('GUI Minimal')


    #membuat label dan menempatkannya ke dalam form pada koordinat(55,44)
    #metode setParent() menentukan bahwa parent dari komponen label adalah form
    label = QLabel('Helo Minimal')
    label.move(55,40)
    label.setParent(form)

    #berguna untuk menampilkan form peserta kontrol-kontrol yang sudah ada di dalamnya
    form.show()

    #merupakan pengulanagn utama (main loop) dari aplikasi.
    #Dengan kode ini, form akan ditampilkan secara terus sampai ada respon-respon
    #tertentu dari user (penggunaan program).
    #Perlu diperhatikan bahwa metode exec_() diakhiri dengan tanda underscore
    #karena dalam Python exec merupakan kata kunci dan memiliki artilain.
    a.exec_()