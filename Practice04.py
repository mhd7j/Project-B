

def decorator(*args):
    def def_1(func):
        
        def def_2(*a):

            print(args[0])
            func(*a)
            print(args[1])
   
        return def_2
    return def_1

@decorator("before" ,"after")
def def_3(name):
    print(f"Hello {name}")

def_3("Bahram")