def lucro_acao(acoes):
    resultado = 0
    menor_valor = min(acoes)
    menor_valor_index = acoes.index(menor_valor)
    possiveis_valores = acoes[menor_valor_index + 1::]
    if len(possiveis_valores) > 0:
        possiveis_valores.sort()
        maior_valor = possiveis_valores[-1]
        resultado = maior_valor - menor_valor

    return resultado