import random

def gerar_cpf(formatado: bool = False) -> str:
    # Gera os 9 primeiros dígitos aleatoriamente
    cpf = [random.randint(0, 9) for _ in range(9)]
    
    # Calcula o primeiro dígito verificador
    for _ in range(2):
        soma = sum(v * ((len(cpf) + 1) - i) for i, v in enumerate(cpf))
        digito = (soma * 10 % 11) % 10
        cpf.append(digito)
        
    resultado = "".join(map(str, cpf))
    if formatado:
        return f"{resultado[:3]}.{resultado[3:6]}.{resultado[6:9]}-{resultado[9:]}"
    return resultado

def gerar_cnpj(formatado: bool = False) -> str:
    # Gera os 12 primeiros dígitos (8 base + 4 filial 0001)
    cnpj = [random.randint(0, 9) for _ in range(8)] + [0, 0, 0, 1]
    
    # Pesos para cálculo dos dígitos verificadores
    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_2 = [6] + pesos_1
    
    # Calcula o primeiro dígito
    soma1 = sum(v * pesos_1[i] for i, v in enumerate(cnpj))
    r1 = soma1 % 11
    d1 = 0 if r1 < 2 else 11 - r1
    cnpj.append(d1)
    
    # Calcula o segundo dígito
    soma2 = sum(v * pesos_2[i] for i, v in enumerate(cnpj))
    r2 = soma2 % 11
    d2 = 0 if r2 < 2 else 11 - r2
    cnpj.append(d2)
    
    resultado = "".join(map(str, cnpj))
    if formatado:
        return f"{resultado[:2]}.{resultado[2:5]}.{resultado[5:8]}/{resultado[8:12]}-{resultado[12:]}"
    return resultado
