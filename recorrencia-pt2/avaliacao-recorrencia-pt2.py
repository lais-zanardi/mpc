def formula_recorrencia(z, n):
    soma, i = 0, 1
    a = z
    b = 2
    while i <= n:
        print(a, ' / ',  b)
        soma += a/b
        a *= (-2)
        b *= (i+2)
        i += 1
    return soma

z = int(input('z: '))
n = int(input('n: '))
print("Soma = " + str(formula_recorrencia(z,n)))