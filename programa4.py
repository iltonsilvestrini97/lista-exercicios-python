def eh_primo(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def testar_primos_1_a_100():
    print("Testando números de 1 a 100:")
    for num in range(1, 101):
        if eh_primo(num):
            print(f"{num} -> Primo")
        else:
            print(f"{num} -> Não primo")

if __name__ == "__main__":
    testar_primos_1_a_100()