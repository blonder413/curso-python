"""
Se debe llamar al commit para que los cambios hagan efecto
Si no se llama al commit el registro se inserta, se aumenta el auto_increment
pero al no haber commit no se guardan los cambios en la base de datos, lo que
hace parecer que no se inserta
"""
from conectar import database, cu

# Insertar un registro
cu.execute("insert into agenda values (%s, %s, %s, %s)", (None, "Jill", "jvalentine@bsaa.org", "1970-04-13"))

# Insertar varios registros
datos = [
    (None, "Claire", "credfield@terrasave.org", "1986-10-08"),
    (None, "Chris", "credfieldd@bsaa.org", "1990-08-17")
]
cu.executemany("insert into agenda values (%s, %s, %s, %s)", datos)

database.commit()
database.close()
