def divisors(num):
    
    # divisors=[]

    # for i in range (1, num+1):
    #     if num % i == 0:
    #         divisors.append(i)

        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors


def run():
    try:
        num = int(input("ingresa un numero: "))
        if num<=0:
            raise  Exception ("Debe ingresar un numero mayor a 0")
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingtresar un número")
    except Exception as ve:
        print(ve)

if __name__ == '__main__':
    run()
