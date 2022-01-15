from db import *

class dosen:
    def __init__(self):
        pass
    def getName(nid):
        sql = "SELECT nama FROM dosen WHERE nid=%s"
        cursor.execute(sql, (nid,))
        return cursor.fetchall()
