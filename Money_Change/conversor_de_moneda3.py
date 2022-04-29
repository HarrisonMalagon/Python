# Creacion de Mensaje de Bienvenida.
menu = """"
Bienvenidos al conversor de monedas💰

   __________  _   ___    ____________ _____ ____  ____       ____  ______     __  _______  _   ____________  ___ 
  / ____/ __ \/ | / | |  / / ____/ __ / ___// __ \/ __ \     / __ \/ ____/    /  |/  / __ \/ | / / ____/ __ \/   |
 / /   / / / /  |/ /| | / / __/ / /_/ \__ \/ / / / /_/ /    / / / / __/      / /|_/ / / / /  |/ / __/ / / / / /| |
/ /___/ /_/ / /|  / | |/ / /___/ _, ____/ / /_/ / _, _/    / /_/ / /___     / /  / / /_/ / /|  / /___/ /_/ / ___ |
\____/\____/_/ |_/  |___/_____/_/ |_/____/\____/_/ |______/_____/__________/_/  /_/\____/_/ |_/_____/_____/_/  |_|
                                                    /_____/          /_____/                                      

1 - Pesos Colombianos 
2 - Pesos Argentinos
3 - Pesos Mexicanos

"""

opcion = input(menu)
##Crear Funcion para convertir moneda
def conversor_de_moneda(pais,valor_dolar):
   pesos = input ("¿Cunatos peso "+pais+" Tienes? : ")
   pesos = float(pesos)
   dolares= pesos/ valor_dolar
   dolares=round(dolares,2)
   dolares=str(dolares)
   print("Tienes $"+ dolares,"dolares")

if opcion=='1':
   conversor_de_moneda("Colombianos",4200)
elif opcion== '2':
   conversor_de_moneda("Argentinos",110.68)

elif opcion== '3':
   conversor_de_moneda("Mexicanos",20)

else:
   print("Porfavor ingresa una opcion correcta")

