def def_1(func):

    def def_2(*a):

        print('before Execution')

        func(*a)

        print('after Excecution')

    return def_2

@def_1
def def_3():
    print("yaa yaa")

def_3()