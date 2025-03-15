# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms

medida_cms = float(input("Por favor, ingresar la medida de la pieza que desea convertir a pulgadas: "))

# Paso 2: Convertir las medidas de centímetros a pulgadas

medida_pulgadas = medida_cms / 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario 

print("Las medidas en pulgadas de la pieza ingresada son:", medida_pulgadas)
