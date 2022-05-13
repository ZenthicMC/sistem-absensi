import mysql.connector

print("Menghubungkan ke database....")
print("(Mohon tunggu hingga 5 detik)")

db = mysql.connector.connect(
    host="#",
    user="#",
    password="#",
    database="#"
)

if(db):
  print("Koneksi sukses terhubung!\n")
else:
  print("Koneksi ke database gagal, pastikan anda memiliki koneksi internet!")
  
cursor = db.cursor()
