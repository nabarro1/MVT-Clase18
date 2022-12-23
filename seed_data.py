from ejemplo.models import Familiar
Familiar(nombre="Ramiro", direccion="Quilmes", numero_pasaporte=123123).save()
Familiar(nombre="Juan", direccion="Quilmes 2", numero_pasaporte=890890).save()
Familiar(nombre="Pelado", direccion="Quilmes 3", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Quilmes 4", numero_pasaporte=567567).save()
print("Se cargo con éxito los usuarios de pruebas")