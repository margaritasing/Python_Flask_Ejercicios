from ejemplo7 import basededatos, Persona


basededatos.create_all()
persona1 = Persona("Libia", 43)
persona2 = Persona("Ana", 54)

basededatos.session.add_all([persona1, persona2])
basededatos.session.commit()

persona3 = Persona("Alexander", 17)
basededatos.session.add(persona3)
basededatos.session.commit()

personas = Persona.query.all()
print("Consultar todas las personas")
print(personas)

filtro1 = Persona.query.filter_by(nombre="Libia")
print("Filtro por nombre = Libia")
print(filtro1.all())

seleccion1 = Persona.query.get(2)
print("Busqueda por Id")
print(seleccion1)

persona = Persona.query.get(1)
persona.edad = 45
basededatos.session.add(persona)
basededatos.session.commit()

persona_borrar = Persona.query.get(3)
basededatos.session.delete(persona_borrar)
basededatos.session.commit()
print("hemos borrado a esta personas {}".format(persona_borrar))

personas = Persona.query.all()
print("Todas las personas")
print(personas)
