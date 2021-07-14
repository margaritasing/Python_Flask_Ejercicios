from ejemplo8 import basededatos, Mascota, Juguete, Propietario

mascota1 = Mascota('Mia')
mascota2 = Mascota('Minina')

basededatos.session.add_all([mascota1, mascota2])
basededatos.session.commit()

mascotas = Mascota.query.all()
print(mascotas)

mascota1 = Mascota.query.filter_by(name='Mia').first()

propietario1 = Propietario('Libia', mascota1.id )
basededatos.session.add_all(propietario1)
basededatos.session.commit()

juguete1 = Juguete('pelota', mascota1.id)
juguete2 = Juguete('peluche', mascota1.id)
basededatos.session.add_all([juguete1, juguete2])
basededatos.session.commit()

mascota = Mascota.query.filter_by(name='Mia').first()
print(mascota)
mascota.mostrar_juguetes()
