def num(n):
    if int(n) > 0:
        for i in range(1, int(n) + 1):
            for j in range(1, i + 1):
                print(j, end=",")
        print()
    if int(n) < 0:
        for i in range(1, -int(n) + 1):
            for j in range(1, i + 1):
                print(-j, end=",")
        print()

# Ejemplo de uso:
num(-4)