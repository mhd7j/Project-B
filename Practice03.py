def def_1(func):
    def def_2(*asghar):
        a = func(*asghar)
        return "WELCOME" + a
    return def_2

@def_1
def greeting(name):
    return name
print(greeting("bahram"))
