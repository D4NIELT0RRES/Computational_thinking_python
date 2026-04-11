def alturaValida(valida):

    if valida < 0.5 or valida > 2.5:
        return False
    return True

def media(valor1, valor2, valor3):

    if alturaValida(valor1) and alturaValida(valor2) and alturaValida(valor3):
        return (valor1 + valor2 + valor3) / 3
    return False

print()