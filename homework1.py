my_list = [121, 233, 42, 22, 43, 334, 54, 254, 55]

def foyiz():
    son = 100
    input1 = int(input("Son kiriting: "))
    index = 0
    while index < len(my_list):
        m = my_list[index] / son * input1
        print(m)
        index += 1

foyiz()