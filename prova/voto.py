def voto(idade):
    if idade < 16:
        return "NÃO PODE VOTAR"
    elif idade == 16 or idade == 17:
        return "PODE VOTAR"
    elif idade >= 18 and idade <= 34:
        return "DEVE VOLTAR MAS NÃO PODE SER PRESIDENTE"
    elif idade > 34 and idade < 70:
        return "DEVE VOTAR E PODE SER PRESIDENTE"
    else:
        return "PODE VOTAR E PODE SER PRESIDENTE"