def funcion_externa():
    variable_local_externa = 'variable local externa'

    def funcion_anidada():
        variable_local_anidada = 'variable local anidada'

        # indicamos que vamos a llamar una variable no definida localmente
        # no debemos incicar nonlocal si no vamos a modificar su valor
        nonlocal variable_local_externa
        variable_local_externa = 'nuevo valor variable local externa'
    
    funcion_anidada()
    print(f'variable local externa: {variable_local_externa}')
funcion_externa()
