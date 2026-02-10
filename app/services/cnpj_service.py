def validar_cnpj(cnpj: str) -> bool:
    cnpj = ''.join(filter(str.isdigit, cnpj))
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False
    pesos_1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    pesos_2 = [6] + pesos_1
    def calc(c, p):
        soma = sum(int(c[i]) * p[i] for i in range(len(p)))
        r = soma % 11
        return '0' if r < 2 else str(11 - r)
    return cnpj[-2:] == calc(cnpj, pesos_1) + calc(cnpj, pesos_2)
