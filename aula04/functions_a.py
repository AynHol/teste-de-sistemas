def person_person(name, phone, age, email):
    return '48' in phone and ' ' in name and '@' in email



def person_values(salary, commission, inss):
    return round(salary+(salary*commission)-(salary*inss), 2)