def colaborador(salario, tempo, matricula):
    if matricula.isdigit() == True:
        cargo = ""
        if salario < 4000 or tempo < 5:
            cargo = "Junior"
        elif salario >= 4000.01 and salario < 10000 or tempo >= 6 and tempo < 10:
            cargo = "Sênior"
        else:
            cargo = "Pleno"
        return cargo
    else:
        return "Matricula invalida"