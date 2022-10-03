import sqlite3
from config import ORIGIN_DATA

def select_all():
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()

    result = cur.execute("SELECT id, date, concept, quantity from movements order by date;")

    filas = result.fetchall()
    columnas = result.description

    resultado = []
    for fila in filas:
        posicion_columna = 0
        d = {}
        for campo in columnas:
            d[campo[0]] = fila[posicion_columna]
            posicion_columna += 1
        resultado.append(d)

    conn.close()
    """
    resultado = []
    for fila in filas:
        d = {}
        for posicion, campo in enumerate(columnas):
            d[campo[0]] = fila[posicion]
        resultado.append(d)

    """

    return resultado

def insert(registro):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()

    cur.execute("INSERT INTO movements (date, concept, quantity) values (?, ?, ?);", registro)
    conn.commit()
    conn.close()


