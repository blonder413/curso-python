def dic(**kwargs):
    return kwargs

print(dic(nombre='blonder', edad=413))

def mostar_texto(nombre=None, *lenguajes, **educacion):
    print(educacion)
    return nombre, lenguajes, educacion

# print(mostar_texto('blonder'))
# print(mostar_texto('blonder', ('php', 'python')))
# print(mostar_texto('blonder', 'php', 'python'))
kwargs = {"nombre": 'blonder', "nick": "blonder413", "edad": 413}
print(mostar_texto(educacion=kwargs))
