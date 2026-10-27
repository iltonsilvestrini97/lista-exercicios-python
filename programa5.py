def inverter_letras_palavras(frase):
    palavras = frase.split()

    palavras_invertidas = [palavra[::-1] for palavra in palavras]

    nova_frase = " ".join(palavras_invertidas)

    return nova_frase

if __name__ == "__main__":
    print("--- Teste do Inversor de Letras ---")
    frase_original = input("Digite uma frase: ")

    resultado = inverter_letras_palavras(frase_original)

    print(f"\nFrase original: {frase_original}")
    print(f"Frase modificada: {resultado}")