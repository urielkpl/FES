###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
tecnic = input("Escriu el nom del tecnic: ")
xarxa = input("Escriu el nom de la xarxa: ")
print("EL tecnic", tecnic, "esta instal·lant la xarxa", xarxa)


# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud = float(input("Escriu la longitud de l'enllaç de fibra en quilòmetres: "))
velocitat = float(input("Escriu la velocitat de transmissió en Gbps: "))
segons = 8 / velocitat_gbps
print(f"L'enllaç de {longitud} km necessita {segons} segons per transmetre 1 GB.")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
preu_hora = float(input("Quin es el preu per hora: "))
hores = int(input("Escriu el número d'hores que triga l'instalació: "))
preu_material = float(input("Escriu el preu del material: "))
preu_total = preu_hora*hores + preu_material
print(f"El preu total de l'instalació és {preu_total} euros")



