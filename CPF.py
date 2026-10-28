# p = peso | d10 = digito 10 | d11 = digito 11 | resultados = lista de multiplicaçoes |  

def validarFUN(cpf):

    DigCPF = []
    for valor in cpf:
        DigCPF.append(valor)

    def ndigitos(lista):
        try:
            lista[10]
            return True 
        except:
            return False

    
    def DecDigito(DigCPF):
        """ calcula o 10 digito para verificar se esta igual o digito do cpf digitado """
        resultados = []
        p = 10
        for i in range(0,9):
            resultados.append(int(DigCPF[i])*p)
            p -=1
        resto = sum(resultados)%11
        if resto < 2:
            d10 = resto
        else:
            d10 = 11 - resto
        if d10 == int(DigCPF[9]):
            return True
        else:
            return False

    def DecPrimDigito(DigCPF):
        """ calcula o 11 digito para verificar se esta igual o digito do cpf digitado """
        resultados = []
        p = 11
        for i in range (0,10):
            resultados.append(int(DigCPF[i])*p)
            p -= 1 
        resto = sum(resultados)%11
        if resto < 2:
            d11 = resto
        else:
            d11 = 11 - resto
        if d11 == int(DigCPF[10]):
            return True
        else:
            return False
    
    if ndigitos(lista=DigCPF) and DecDigito(DigCPF=DigCPF) and DecPrimDigito(DigCPF=DigCPF):
        return True
    else: return False
    