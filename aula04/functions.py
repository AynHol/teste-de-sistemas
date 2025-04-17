def gravar(name, age, email, phone):
    tudo = {"nome": name,"idade": age,"email": email,"telefone": phone}
    if " " in name and age and "@" in email and "48" in phone:
        return tudo
    else:
        return "Dados incorretos"

def receber(salario, comissao, inss):
    primeiro = salario + (salario * comissao)
    segundo = (salario * inss)
    final = primeiro - segundo
    return round(final,2)

print(receber(1700,500,600))