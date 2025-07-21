valores = [True,False,True,False,True]
contT = 0
contF = 0
for valor in valores:
        if valor == True :
            contT += 1
        else:
            contF += 1

print(f"Quantidade de True: {contT}")
print(f"Quantidade de False: {contF}")
