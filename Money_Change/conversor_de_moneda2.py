
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

if opcion=='1':
   pesos = input ("¿Cunatos peso Colombianos Tienes? : ")
   pesos = float(pesos)
   valor_dolar = 4200
   dolares= pesos/ valor_dolar
   dolares=round(dolares,2)
   dolares=str(dolares)
   print("Tienes $"+ dolares,"dolares")
elif opcion== '2':
   pesos = input ("¿Cunatos peso Argentinos Tienes? : ")
   pesos = float(pesos)
   valor_dolar = 110.68
   dolares= pesos/ valor_dolar
   dolares=round(dolares,2)
   dolares=str(dolares)
   print("Tienes $"+ dolares,"dolares")
elif opcion== '3':
   pesos = input ("¿Cunatos peso Mexicanos Tienes? : ")
   pesos = float(pesos)
   valor_dolar = 20
   dolares= pesos/ valor_dolar
   dolares=round(dolares,2)
   dolares=str(dolares)
   print("Tienes $"+ dolares,"dolares")
else:
   print("Porfavor ingresa una opcion correcta")


