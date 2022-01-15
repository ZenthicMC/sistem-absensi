from db import *

class matkul:
    def __init__(self):
        pass

    def setData(self,nid,nama,sks):
        sql = "INSERT INTO matkul (nid,nama,sks) VALUES (%s,%s,%s)"
        cursor.execute(sql, (nid,nama,sks,))
        db.commit()
        return print("Data matkul {} Berhasil Di Tambah!".format(nama))

    def getData(self):
        sql = '''SELECT matkul.id_matkul,matkul.nama,dosen.nama,matkul.sks FROM matkul
        INNER JOIN dosen ON matkul.nid = dosen.nid ORDER BY matkul.id_matkul'''
        cursor.execute(sql)
        return cursor.fetchall()

    def deleteData(self,id):
        sql = "DELETE FROM matkul WHERE id_matkul=%s"
        cursor.execute(sql, (id,))
        db.commit()
        return print("Data matkul {} Berhasil Di hapus!".format(id))

    def verifyNID(nid):
        cursor.execute('SELECT * FROM dosen WHERE nid = %s', (nid,))
        if cursor.fetchall():
            return True
        else:
            return False

    def verifyIDMatkul(id_matkul):
        cursor.execute('SELECT * FROM matkul WHERE id_matkul = %s', (id_matkul,))
        if cursor.fetchall():
            return True
        else:
            return False

