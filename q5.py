peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25.0:
    print("Classificação: Peso normal")
elif imc < 30.0:
    print("Classificação: Sobrepeso")
elif imc < 35.0:
    print("Classificação: Obesidade grau 1")
elif imc < 40.0:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3 (mórbida)")