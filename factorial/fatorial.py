def fatorial(numero):
    if numero < 2:
        return 1
    else:
        return numero * fatorial(numero-1)