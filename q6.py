n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("Por favor, digite um número positivo.")
else:
    soma = 0
    for i in range(2, n + 1, 2):  
        soma += i

    print("Soma dos números pares:", soma)
