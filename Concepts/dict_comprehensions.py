#crear diccionario con las llaves 100 naturales y valores 100n  al cubo

def run():
    # my_dict={}
    # for i in range(1,101):
    #     if i%3 != 0:
    #         my_dict[i]=i**3
    # print(my_dict)
    my_dict ={i: i**3 for i in range (1,101) if i%3 !=0}
    print(my_dict)

if __name__=='__main__':
    run()