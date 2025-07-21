total = int(input("Digite o valor total da compra: "))
pago = int(input("Digite o valor pago :"))

if pago > total:
    troco = pago - total
    print(f"Troco: {troco:.2f}")
elif pago == total:
    print("Não há troco")
else:
    falta = total - pago
    print(f"Valor insulficiente, faltam {falta:.2f}")