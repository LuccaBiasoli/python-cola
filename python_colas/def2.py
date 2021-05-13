funcmes = [('vitor', 100), ('rafael', 320) , ('lucca', 400)]


def funcionario_mes (funcmes):
    atual_max = 0
    func_do_mes = ''

    for funcs, horas in (funcmes):
        if horas > atual_max:
            atual_max = horas
            func_do_mes = funcs 
        else:
            pass

    return (func_do_mes, atual_max)

res_func = funcionario_mes(funcmes)
print(res_func)


################# 
# MESMO EXEMPLO QUE EM CIMA SO QUE SALVANDO SEPARADAMENTE NO FINAL 

funcmes = [('vitor', 100), ('rafael', 320) , ('lucca', 400)]


def funcionario_mes (funcmes):
    atual_max = 0
    func_do_mes = ''

    for funcs, horas in (funcmes):
        if horas > atual_max:
            atual_max = horas
            func_do_mes = funcs 
        else:
            pass

    return (func_do_mes, atual_max)

funcs , horas = funcionario_mes (funcmes)
print(funcs)