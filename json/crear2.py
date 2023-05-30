import json
archivo = open("/home/blonder413/Python/biblioteca-python/json/miarchivo.json", "w+")
info = {
    "nombre": "blonder",
    "nick": "blonder413",
    "numero": 413,
    "web": "blonder413.wordpress.com"
}
json.dump(info, archivo)
