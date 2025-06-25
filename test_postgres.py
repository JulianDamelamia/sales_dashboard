import psycopg2

try:
    conn = psycopg2.connect(
        dbname="sales_db",
        user="bi_user",
        password="1234",
        host="localhost",
        port="5432"
    )
    print("Conexión exitosa a PostgreSQL")
    conn.close()
except Exception as e:
    print("Error al conectar:", e)