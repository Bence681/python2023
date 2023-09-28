def pitagoraszi_szamharmasok(max_c):
    szamharmasok = []
    for c in range(1, max_c + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a**2 + b**2 == c**2:
                    szamharmasok.append((a, b, c))
    return szamharmasok

max_c = int(input("Adja meg a maximális c értéket: "))
eredmeny = pitagoraszi_szamharmasok(max_c)
print("Pitagoraszi számhármasok:")
for szamharmas in eredmeny:
    print(szamharmas)
