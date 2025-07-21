def maior_numero (n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print(f"Maior valor: {n1}")
    elif n2 > n1 and n2 > n3:
        print(f"Maior valor: {n2}")
    elif n3 > n1 and n3 > n2:
        print(f"Maior valor: {n3}")
maior_numero (2,4,7)