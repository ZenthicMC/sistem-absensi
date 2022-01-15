from db import *

class mahasiswa:
    def __init__(self):
        pass

    def setData(self,nama,alamat,angkatan,email,tgl_lahir,tmpt_lahir):
        sql = "INSERT INTO mahasiswa (nama,alamat,angkatan,email,tgl_lahir,tmpt_lahir) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (nama,alamat,angkatan,email,tgl_lahir,tmpt_lahir,))
        db.commit()
        return print("Data Mahasiswa {} Berhasil Di Tambah!".format(nama))

    def editData(self,npm,nama,alamat,angkatan,email,tgl_lahir,tmpt_lahir):
        sql = "UPDATE mahasiswa SET nama= %s, alamat= %s, angkatan= %s, email= %s, tgl_lahir= %s, tmpt_lahir= %s WHERE npm= %s"
        cursor.execute(sql, (nama,alamat,angkatan,email,tgl_lahir,tmpt_lahir,npm,))
        db.commit()
        return print("Data Mahasiswa {} Berhasil Di Edit!".format(nama))

    def getData(self,angkatan):
        sql = "SELECT * FROM mahasiswa WHERE angkatan=%s ORDER BY npm"
        cursor.execute(sql, (angkatan,))
        return cursor.fetchall()

    def deleteData(self,npm):
        sql = "DELETE FROM mahasiswa WHERE npm= %s"
        cursor.execute(sql, (npm,))
        db.commit()
        return print("Data Mahasiswa {} Berhasil Di hapus!".format(npm))

    def getName(self,npm):
        sql = "SELECT nama FROM mahasiswa WHERE npm=%s"
        cursor.execute(sql, (npm,))
        return cursor.fetchall()

    


