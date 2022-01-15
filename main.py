import os
from mahasiswa import mahasiswa
from matkul import matkul
from db import *
from absen import code
from dosen import dosen

mh = mahasiswa()
mk = matkul()
absen = code(111111,999999)

npm = 0
nid = 0
role = ''

# Fungsi untuk login mahasiswa & dosen
def login():
    global npm, nid
    global role
    print("======================================")
    print("\t\tLogin")
    print("======================================")
    id = int(input('Masukkan NPM/NID: '))
    password = int(input('Masukkan Tgl Lahir: '))
    role = input('Masuk sebagai dosen / mahasiswa ?: ')
    print("======================================")

    if role == 'dosen' or role == 'Dosen':
        cursor.execute('SELECT * FROM dosen WHERE nid = %s AND tgl_lahir = %s', (id, password))
        if cursor.fetchall():
            nid = id
            menuDosen()
        else:
            print('\nInvalid Credentials!\n')
            login()
    elif role == 'mahasiswa' or role == 'Mahasiswa':
        cursor.execute('SELECT * FROM mahasiswa WHERE npm = %s AND tgl_lahir = %s', (id, password))
        if cursor.fetchall():
            npm = id
            menuMahasiswa()
        else:
            print('\nInvalid Credentials!\n')
            login()
    

# Fungsi untuk menanyakan kepada user jika ingin kembali ke menu utama
def pause():
    pilihan = input("Ingin kembali ke menu utama? (Y/N) ")
    if(pilihan=="Y" or pilihan=="y"):
        if role == 'dosen' or role == 'Dosen':
            os.system("cls")
            menuDosen()
        elif role == 'mahasiswa' or role == 'Mahasiswa':
            os.system("cls")
            menuMahasiswa()
    elif(pilihan=="N" or pilihan=="n"):
        quit()


# Fungsi untuk menampilkan menu dosen    
def menuDosen():
    os.system('cls')
    nama_dosen = dosen.getName(nid)
    print("=================================")
    print("\t Menu Dosen")
    print("=================================")
    for nama in nama_dosen:
         print("Selamat datang {} !".format(nama[0]))
    print("\nMenu Mahasiswa:")
    print(" [1] Tambah Mahasiswa")
    print(" [2] Edit Mahasiswa")
    print(" [3] Hapus Mahasiswa")
    print(" [4] Lihat Mahasiswa")
    print("Menu Absensi:")
    print(" [5] Buat Kode Absen")
    print(" [6] Hapus Kode Absen")
    print("Menu Mata Kuliah:")
    print(" [7] Tambah Matakuliah")
    print(" [8] Lihat Matakuliah")
    print(" [9] Hapus Matakuliah")
    print("\n[0] Keluar Program")
    print("=================================")
    pilihan = int(input("Pilihan >> "))

    if pilihan == 1:
        tambahMahasiswa()
    elif pilihan == 2:
        editMahasiswa()
    elif pilihan == 3:
        hapusMahasiswa()
    elif pilihan == 4:
        lihatMahasiswa()
    elif pilihan == 5:
        buatKodeAbsen()
    elif pilihan == 6:
        hapusKodeAbsen()
    elif pilihan == 7:
        tambahMatkul()
    elif pilihan == 8:
        lihatMatkul()
    elif pilihan == 9:
        hapusMatkul()
    elif pilihan == 0:
        quit()
    else:
        print("Invalid Input!")


# Fungsi untuk menambahkan data mahasiswa
def tambahMahasiswa():
    print("=================================")
    print("\tTambah Mahasiswa") 
    print("=================================")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    angkatan = input("Masukkan Angkatan: ")
    email = input("Masukkan Email: ")
    tgl_lahir = input("Masukkan Tanggal Lahir (Cth: 12062003): ")
    tmpt_lahir = input("Masukkan Tempat Lahir: ")
    print("=================================")
    mh.setData(nama,alamat,angkatan,email,tgl_lahir,tmpt_lahir)
    pause()


# Fungsi untuk mengedit data mahasiswa
def editMahasiswa():
    print("=================================")
    print("\tEdit Mahasiswa") 
    print("=================================")
    npm = input("Masukkan NPM: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    angkatan = input("Masukkan Angkatan: ")
    email = input("Masukkan Email: ")
    tgl_lahir = input("Masukkan Tanggal Lahir: ")
    tmpt_lahir = input("Masukkan Tempat Lahir: ")
    print("=================================")
    mh.editData(npm,nama,alamat,angkatan,email,tgl_lahir,tmpt_lahir)
    pause()


# Fungsi untuk menghapus data mahasiswa berdasarkan npm
def hapusMahasiswa():
    print("=================================")
    print("\tHapus Mahasiswa") 
    print("=================================")
    npm = input("Masukkan NPM: ")
    print("=================================")
    mh.deleteData(npm)
    pause()


# Fungsi untuk melihat data mahasiswa berdasarkan angkatan
def lihatMahasiswa():
    print("=================================")
    print("\tLihat Mahasiswa") 
    print("=================================")
    angkatan = input("Masukkan Angkatan: ")
    print("=================================")

    os.system('cls')
    listdata = mh.getData(angkatan)
    print("=======================================================================================================")
    print("\t\t\t\t\tLihat Mahasiswa")
    print("=======================================================================================================")
    print("{:<6} {:<25} {:<12} {:<12} {:<20} {:<14} {:<12}".format('NPM','Nama','Alamat','Angkatan','Email','Tgl Lahir','Tmpt Lahir'))
    for data in listdata:
        print("{:<6} {:<25} {:<12} {:<12} {:<20} {:<14} {:<12}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
    print("=======================================================================================================")
    pause()


# Fungsi Untuk Membuat Kode Absen Random Dengan Range 111111 - 999999
def buatKodeAbsen():
    kode = code(111111,999999)
    print("================================")
    print("Buat Kode Absensi")
    print("================================")
    input_kode_matkul = int(input("Masukkan Kode Matkul: "))

    if matkul.verifyIDMatkul(input_kode_matkul) == True:
        pass
    elif matkul.verifyIDMatkul(input_kode_matkul) == False:
        print("Kode Matkul tidak dapat ditemukan!")
        buatKodeAbsen()

    os.system('cls')
    print("================================")
    print("Kode Absensi:")
    print(code.getCode(kode,input_kode_matkul))
    print("================================")
    pause()

# Fungsi untuk menghapus kode absensi
def hapusKodeAbsen():
    print("================================")
    print("Hapus Kode Absensi")
    print("================================")
    input_kode_absen = int(input("Masukkan Kode Absen: "))
    code.deleteAbsen(input_kode_absen)
    pause()


# Fungsi untuk menampilkan menu mahasiswa
def menuMahasiswa():
    os.system('cls')
    nama_mhsw = mh.getName(npm)
    print("=================================")
    print("\t Menu Mahasiswa")
    print("=================================")
    for nama in nama_mhsw:
         print("Selamat datang {} !".format(nama[0]))
    print("\n[1] Lihat Matkul")
    print("[2] Lihat Absensi")
    print("[3] Lakukan Absen")
    print("\n[0] Keluar Program")
    print("=================================")
    pilihan = int(input("Pilihan >> "))

    if pilihan == 1:
        lihatMatkul()
    elif pilihan == 2:
        lihatAbsensi()
    elif pilihan == 3:
        absensi()
    elif pilihan == 0:
        quit()
    else:
        print("Invalid Input!")

# Fungsi Untuk Mahasiswa Melihat Status Absensi
def lihatAbsensi():
    data_absen = code.getAbsen(npm)
    print("==================================================================")
    print("| {:<30} | {:<8} | {:<18} |".format('Mata Kuliah','Status','Tanggal Absen'))
    print("==================================================================")
    for absen_mhsw in data_absen:
        print("| {:<30} | {:8} | {:<18} |".format(absen_mhsw[0],absen_mhsw[1],absen_mhsw[2]))
    print("==================================================================")
    pause()


# Fungsi Untuk Mahasiswa Melakukan Absensi
def absensi():
    print("========================================")
    print("\t\tAbsensi")
    print("========================================")
    input_kode = int(input("Masukkan Kode Absen: "))
    input_kode_matkul = int(input("Masukkan Kode Matkul: "))
    status = input("Masukkan Status (H/I/A): ")
    print("========================================")
    
    if code.verifyCode(input_kode,input_kode_matkul) == True:
        code.saveAbsen(npm,input_kode_matkul,status)
        pause()
    elif code.verifyCode(input_kode,input_kode_matkul) == False:
        print("Kode absenmu tidak valid!")
        pause()



# Fungsi untuk menambahkan data matkul
def tambahMatkul():
    print("=================================")
    print("\tTambah Matkul") 
    print("=================================")
    id = int(input("Masukkan ID Dosen Pengampu: "))
    nama = input("Masukkan Nama Matkul: ")
    sks = input("Masukkan Jumlah SKS: ")
    print("=================================")

    if matkul.verifyNID(id) == True:
        mk.setData(id,nama,sks)
        pause()
    elif matkul.verifyNID(id) == False:
        print("ID Dosen tidak dapat tidak ditemukan!")
        pause()
        

# Fungsi untuk melihat semua data matkul
def lihatMatkul():
    listdata = mk.getData()
    print("=============================================================")
    print("\t\t\tLihat Matkul")
    print("=============================================================")
    print("{:<3} {:<25} {:<18} {:<15}".format('ID','Nama Matkul','Dosen Pengampu','SKS'))
    for data in listdata:
        print("{:<3} {:<25} {:<18} {:<15}".format(data[0],data[1],data[2],data[3]))
    print("=============================================================")
    pause()


# Fungsi untuk menghapus data matkul berdasarkan id matkul
def hapusMatkul():
    print("=================================")
    print("\tHapus Matkul") 
    print("=================================")
    id = input("Masukkan ID Matkul: ")
    print("=================================")
    mk.deleteData(id)
    pause()


# Menjalankan Program
login()