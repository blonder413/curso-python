from conexion import Conexion
from cursor import Cursor
from persona import Persona
from logger_base import log

class PersonaDao:
    '''
    DAO (Data Access Object)
    CRUD (Create - Read - Update - Delete)
    '''
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        with Cursor() as cursor:
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls, persona):
        with Cursor() as cursor:
            log.debug(f'Persona a insertar: {persona}')
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls.__INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, persona):
        with Cursor() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls.__ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, persona):
        with Cursor() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls.__ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount

if __name__ == '__main__':
    # persona1 = Persona(nombre='helena', apellido='harper', email='hharper@presidence.org')
    # personas_insertadas = PersonaDao.insertar(persona1)
    # log.debug(f'Personas insreadas: {personas_insertadas}')

    # persona1 = Persona(2, 'barry', 'burton', 'bburton@bsaa.org')
    # personas_actualizadas = PersonaDao.actualizar(persona1)
    # log.debug(f'Persona actualizada: {personas_actualizadas}')

    # persona1 = Persona(id_persona=14)
    # persona_eliminada = PersonaDao.eliminar(persona1)
    # log.debug(f'Personas elimnadas: {persona_eliminada}')

    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)
