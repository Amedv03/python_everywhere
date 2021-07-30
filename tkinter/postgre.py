import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="compulab", host="127.0.0.1", port="5432")

print("Database opened successfully")

cur = con.cursor()

'''
cur.execute('''CREATE TABLE SOLICITUD
      (NUM_CUENTA INT PRIMARY KEY     NOT NULL,
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


cur.execute("INSERT INTO STUDENT (NUM_CUENTA,NOMBRE,CANTIDAD_LETRA,CANTIDAD_NUM,
FECHA,CONCEPTO,NOM_CUENTA,DEBITO,CREDITO,BANCO,SOLICITADO_POR,CONSULTADO_POR,
CONFECCIONADO_POR) VALUES (543465,'Amed','doscientos',200,2021-07-30 11:34:00,
'concepto de pruba','compulab',200,500,'General','Amed','Vanesa','Vanesa')");

con.commit()
print("Records inserted successfully")
con.close()