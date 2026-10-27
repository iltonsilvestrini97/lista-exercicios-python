def encontrar_menor():
    print("Digite três números inteiros:")
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))
    n3 = int(input("Terceiro número: "))

    menor = min(n1, n2, n3)

    print(f"\nO menor número entre {n1}, {n2} e {n3} é: {menor}")

if __name__ == "__main__":
    encontrar_menor()
