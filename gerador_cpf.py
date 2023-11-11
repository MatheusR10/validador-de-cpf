primeiro_digito = -1
segundo_digito = -1
str_cpf = ''

while True:
    cont = 10
    sum = 0
    index = 0

    try:
        str_cpf = input('Por favor digite o seu cpf:') 
        nove_digitos = str_cpf[:9]       
        #CALCULANDO O PRIMEIRO DÍGITO
        
        while index < len(nove_digitos):
            sum += (cont*int(nove_digitos[index]))
            cont -= 1 
            index += 1

        sum = sum * 10
        resto = sum % 11

        if resto > 9:
            primeiro_digito = 0
        else:
            primeiro_digito = resto        
       
        #CALCULANDO O SEGUNDO DÍGITO
        cont = 11
        sum = 0
        index = 0
        
        nove_digitos += str(primeiro_digito)
        while index < len(nove_digitos):            
            sum += (cont*int(nove_digitos[index]))
            cont -= 1 
            index += 1

        sum = sum * 10
        resto = sum % 11

        if resto > 9:
            segundo_digito = 0
        else:
            segundo_digito = resto
        
        nove_digitos += str(segundo_digito)
        print(f'CPF VÁLIDO GERADO: {nove_digitos}')
        
    except IndexError:
        print('Erro de indice')