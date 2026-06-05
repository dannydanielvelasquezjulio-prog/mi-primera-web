import random
import string
def generar_contrasena(longitud):
# combina letras,numeros y simbolos
caracteres = string.ascii_letters + string.digits + string.punctuation
#seleccionar caracteres al azar
contrasena = ''.join(random.choice(caracteres) for _ in range(longitud)
return contrasena

if __name__=="__main__":
print("--- ¡Bienvenidos al Generador de Contraseñas! ---")
largo = int(input("Introduce la longitud de la contraseña (ej. 12): "))
nueva_contrasena = generar_contrasena(largo)
print(f"Tu nueeva contraseña segura es: {nueva_contrasena}")
