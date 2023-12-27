import psycopg2
import psycopg2.extras


# Função para conectar ao banco
def conecta_db():
    con = psycopg2.connect(
        host="localhost", database="adm_simcc", user="postgres", password="root"
    )
    return con


# Função para inserir dados
def execScript_db(sql):
    con = conecta_db()
    cur = con.cursor()

    try:
        cur.execute(sql)
        con.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1

    cur.close()
    con.close()


# Função para consultas
def consultar_db(sql):
    try:
        con = conecta_db()
        cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(sql)
        recset = cur.fetchall()
        registros = []

        for rec in recset:
            registros.append(rec)

        con.close()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1

    return registros
