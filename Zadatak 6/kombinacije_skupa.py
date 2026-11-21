# m-kombinacije skupa (bez ponavljanja) pomocu generatornih funkcija.
from itertools import combinations
from math import comb
from stepeni_redovi import mnozi

if __name__ == "__main__":
    # Svaki element skupa daje faktor (1 + x): nije izabran ili jeste izabran.
    for n in range(1, 8):
        p = [1]
        for _ in range(n):
            p = mnozi(p, [1, 1], n)
        assert p == [comb(n, m) for m in range(n + 1)]
        for m in range(n + 1):
            assert p[m] == len(list(combinations(range(n), m)))
    print("(1 + x)^n daje broj m-kombinacija skupa od n elemenata, n = 1..7. OK")

    skup = ["a", "b", "c"]
    print("2-kombinacije skupa {a, b, c}:",
          ["".join(c) for c in combinations(skup, 2)])
    p = [1]
    for _ in range(3):
        p = mnozi(p, [1, 1], 3)
    print("(1 + x)^3 =", p)

    # Skup od 5 elemenata, trazimo 3-kombinacije koje sadrze element a.
    # Za a je faktor x, za ostala cetiri elementa (1 + x).
    p = [0, 1]
    for _ in range(4):
        p = mnozi(p, [1, 1], 5)
    print("x(1 + x)^4 =", p, " koeficijent uz x^3:", p[3])
    broj = sum(1 for c in combinations("abcde", 3) if "a" in c)
    assert p[3] == broj == 6
    print("Prebrojavanje redom daje isto:", broj)

    # Zbir svih koeficijenata je broj svih podskupova (x = 1)
    n = 6
    p = [1]
    for _ in range(n):
        p = mnozi(p, [1, 1], n)
    assert sum(p) == 2 ** n
    print("Za n = 6 zbir koeficijenata je", sum(p), "= 2^6")
    print("Sve provere prosle. OK")
