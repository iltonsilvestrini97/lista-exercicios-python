import math

def verificar_triangulo():
  print("Digite três valores inteiros e positivos:")
  a = int(input("Valor de a: "))
  b = int(input("Valor de b: "))
  c = int(input("Valor de c: "))

  if (a + b > c) and (a + c > b) and (b + c > a):
    print("\nOs valores formam um triângulo!")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(f"A área do triângulo é: {area:.2f}")
  else:
    print("\nOs valores NÃO formam um triângulo.")
    print(f"Valores lidos: a = {a}, b = {b}, c = {c}")

if __name__ == "__main__":
    verificar_triangulo()