import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    conexion.autocommit = False

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Carlos', 'Lara', 'clara@correo.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Juarez', 'jcjuarez@correo.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print('Termina la transaccion, se hizo commit')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()
# insert, update, delete tienen que estar dentro del bloque para que tengan algun cambio
'''
Practicas con with
Para manejo de recursos con mejores practicas
try:
    with conexion:
        with cursor = conexion.cursor() as cursor:
            
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'arojas@correo.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan', 'Perez', 'jperez@correo.com', 1)
            cursor.execute(sentencia, valores)


except Exception as e:
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()
    print('Termina la transaccion, se hizo commit')
'''