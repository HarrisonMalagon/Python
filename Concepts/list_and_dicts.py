def run():
    my_ist=[1,"Hello",True,3.14159]
    my_dict={"firstname":"John","lastname":"Doe"}

    super_list=[
        {"firstname":"Daniel","lastname":"Torres","age":25},
        {"firstname":"Harrison","lastname":"Sanchez","age":24},
        {"firstname":"Miguel","lastname":"Rodriguez","age":23},
        {"firstname":"Jose","lastname":"Garcia","age":22},
        {"firstname":"Rafael","lastname":"Alvarez","age":21},
        {"firstname":"Juan","lastname":"Perez","age":26},
    ]
    super_dict={
        "natural_nums":[1,2,3,4,5,6,7,8,9],
        "integger_nums":[-2,-1,0,1,2,3,4],
        "float_nums":[-2.5,-1.5,0.0,1.5,2.5,3.5,4.5],
    }


    # print(my_ist)
    for key, value in super_dict.items():
        print(f"{key}:{value}")
        # print(key,"-",value)


    # print(super_dict)
    for iTEMS in super_list:
        print(iTEMS["firstname"], iTEMS["lastname"],"-",iTEMS["age"])
    print(iTEMS.keys())


if __name__ == '__main__':
    run()