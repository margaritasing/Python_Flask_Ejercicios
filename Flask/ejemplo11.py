from werkzeug.security import generate_password_hash, check_password_hash

password = 'clavesecreta2'

password_encriptada = generate_password_hash(password)


verificar= check_password_hash(password_encriptada, 'clave2')

verificar= check_password_hash(password_encriptada, 'clavesecreta1')
print(password_encriptada)
