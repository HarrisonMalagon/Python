# with open(<ruta>, <modo_apertura>) as <nombre>

import numbers


def read_file ():
    numbers=[]
    with open ('./archivos/numbers.txt', 'r', encoding="UTF-8") as f:
        # print (f.read())
        for line in f:
            numbers.append(int(line))
    print (numbers)


def write_file ():
    names=['Juan', 'Pedro', 'Maria', 'Ana', "Rocío","Nicolas","José"]
    # with open ('./archivos/names.txt', 'w') as f:
    # with open ('./archivos/names.txt', 'w', encoding="UTF-8") as f:
    with open ('./archivos/names.txt', 'a', encoding="UTF-8") as f:
        # f.write('Hola mundo')
        for name in names:
            f.write(name + '\n')
        print (f.name)

def run ():
    # read_file()
    write_file()

if __name__ == '__main__':
    run()