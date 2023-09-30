import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
conexion2 = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

"""
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Proporciona el valor id_persona: ')
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
# un cursor es un objeto que va a permitir ejecutar sentencias SQL
# permite recuperar todos los registros de la sentencia que se ha ejecutado
# %s placeholder, parametro posicional, fetchall o fetchone

try:
    with conexion2:
        with conexion2.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # llaves_primarias = ((1, 2, 3),)
            entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion2.close()
"""
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('Angel', 'Quintana', 'aquintana@correo.com'),
                ('Marcos', 'Cantu', 'mcantu@correo.com'),
                ('Maria', 'Gonzalez', 'mgonzalez@correo.com')
            )
            cursor.executemany(sentencia, valores)
            # conexion.commit(), al usar with el commit es automatico
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
