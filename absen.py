from db import *
import random
import datetime

class code:
    def __init__(self,range1,range2):
        self.range1 = range1
        self.range2 = range2 

    def getCode(self,id_matkul):
        code = random.randint(self.range1, self.range2)
        sql = "INSERT INTO active_codes (code,id_matkul) VALUES (%s, %s)"
        cursor.execute(sql, (code,id_matkul,))
        db.commit()
        return code

    def verifyCode(kode,id_matkul):
        cursor.execute('SELECT * FROM active_codes WHERE code = %s AND id_matkul = %s', (kode, id_matkul,))
        if cursor.fetchall():
            return True
        else:
            return False

    def saveAbsen(npm,id_matkul,status):
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        sql = "INSERT INTO kehadiran (npm,id_matkul,status,tgl_absen) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (npm,id_matkul,status,date))
        db.commit()
        return print("Kamu berhasil melakukan absensi!")

    def getAbsen(npm):
        sql = '''SELECT matkul.nama,kehadiran.status,kehadiran.tgl_absen FROM matkul
        INNER JOIN kehadiran ON matkul.id_matkul = kehadiran.id_matkul WHERE kehadiran.npm = %s ORDER BY kehadiran.tgl_absen'''
        cursor.execute(sql, (npm,))
        return cursor.fetchall()

    def deleteAbsen(kode):
        sql = "DELETE FROM active_codes WHERE code= %s"
        cursor.execute(sql, (kode,))
        db.commit()
        return print("Kode Absensi {} Berhasil Di hapus!".format(kode))

