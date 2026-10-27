def converter_idade():
    total_dias = int(input("Digite a idade expressa em dias: "))

    anos = total_dias // 365
    resto_dias = total_dias % 365

    meses = resto_dias // 30
    dias = resto_dias % 30

    print(f"\n{total_dias} dias equivalem a:")
    print(f"- {anos} ano(s)")
    print(f"- {meses} mes(es)")
    print(f"- {dias} dia(s)")


if __name__ == "__main__":
    converter_idade()