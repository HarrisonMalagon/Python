def run():
    diccionario = {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'edad': 23,
        'cedula': '12345678',
        'direccion': 'Calle falsa 123',
        'telefono': '12345678',
        'email': 'juan.perez@fake.com',
    }
    poblacion_de_paises = {
        'Argentina': 45195774 ,
        'Brasil': 20000000,
        'Chile': 19116201 ,
        'Colombia': 50882891,
        'Ecuador': 212559417,
        'Peru': 33149016,
    }
    # print(diccionario)
    # print(diccionario['nombre'])
    # print(diccionario['cedula'])
    # print("La poblacion de Argentia es de",str(poblacion_de_paises['Argentina']) + " de habitantes")
    
    # for pais in poblacion_de_paises.keys():
    #     print(pais)

    # for pais in poblacion_de_paises.values():
    #     print(pais)

    # for pais in poblacion_de_paises.items():
    for pais,poblacion in poblacion_de_paises.items():
        print(pais +' tiene '+ str(poblacion) + ' habitantes')
       


if __name__ == '__main__':
    run()