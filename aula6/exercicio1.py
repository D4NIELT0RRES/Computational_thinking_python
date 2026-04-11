def tel_valido(string):
    tamanho = len(string)
    if tamanho < 8:
        return False
    elif tamanho > 11:
        return False
    else:
        return True
    
assert(tel_valido("123") == False)
assert(tel_valido("1133334444") == False)