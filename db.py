import mysql.connector

print("Menghubungkan ke database online....")
print("(Mohon tunggu hingga 5 detik)")

db = mysql.connector.connect(
    host="db.jaraya.my.id",
    user="user_absensi",
    password="absensi123",
    database="absen"
)

if(db):
  print("Koneksi sukses terhubung!\n")
else:
  print("Koneksi ke database gagal, pastikan anda memiliki koneksi internet!")
  
cursor = db.cursor()
