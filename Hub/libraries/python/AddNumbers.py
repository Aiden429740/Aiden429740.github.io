while True:
    value1 = int(input("Value 1: "))
    value2 = int(input("Value 2: "))

    if value1 == 0:
        quit()
    
    if value1 < 100:
        quit()
    elif value2 < 100:
        quit()
    if value1 > 999:
        quit()
    elif value2 > 999:
        quit()
    
    def calc():
        t = value1 + value2
        print(t)

    calc()
