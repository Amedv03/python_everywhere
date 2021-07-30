import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="compulab", host="127.0.0.1", port="5432")

print("Database opened successfully")
'''
cur = con.cursor()

cur.execute('''CREATE TABLE SOLICITUD
      (NUM_CUENTA VARCHAR(50) PRIMARY KEY     NOT NULL,
      NOMBRE           TEXT    NOT NULL,
      CANTIDAD_LETRA    TEXT     NOT NULL,
      CANTIDAD_NUM      INT     NOT NULL,
      FECHA           TIMESTAMP    NOT NULL,
      CONCEPTO        TEXT     NOT NULL,
      NOM_CUENTA       TEXT NOT NULL,
      DEBITO           INT,
      CREDITO           INT,
      BANCO           TEXT    NOT NULL,
      SOLICITADO_POR           TEXT    NOT NULL,
      AUTORIZADO_POR           TEXT    NOT NULL,
      CONFECCIONADO_POR           TEXT    NOT NULL);''')
print("Table created successfully")
'''

con.commit()
print("Records inserted successfully")
con.close()