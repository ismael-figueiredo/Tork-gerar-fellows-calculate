def encontrar_combinacoes_de_engrenagens(relacao_dentes_alvo, engrenagens_disponiveis):
    combinacoes_validas = []
    for A in engrenagens_disponiveis:
        for B in engrenagens_disponiveis:
            for C in engrenagens_disponiveis:
                for D in engrenagens_disponiveis:
                    if (C + D) == 120:  
                        if (C * A) / (D * B) == relacao_dentes_alvo:
                            combinacoes_validas.append((A, B, C, D))
    return combinacoes_validas

def principal():
    engrenagens_disponiveis = [25,27,28,30,32,37,39,40,42,43,46,48,49,51,54,58,60,62,63,66,68,70,72,73,76,80,90]
    Zs = int(input("Digite o número de dentes da peça (Zs): "))
    Z = int(input("Digite o número de dentes do cortador (Z): "))
    
    relacao_alvo = Zs / Z
    
    print(f"Calculando combinações de engrenagens para uma relação alvo de {relacao_alvo:.2f}")
    combinacoes = encontrar_combinacoes_de_engrenagens(relacao_alvo, engrenagens_disponiveis)
    
    if combinacoes:
        print("Foram encontradas as seguintes combinações de engrenagens (A, B, C, D):")
        for combinacao in combinacoes:
            print(combinacao)
    else:
        print("Não foram encontradas combinações válidas para a relação de dentes dada.")

if __name__ == "__main__":
    principal()



