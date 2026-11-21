# Celobrojne jednacine i generatorne funkcije.
from itertools import product
from math import comb
from stepeni_redovi import broj_resenja, mnozi

if __name__ == "__main__":
    # x1 + x2 + x3 = 10, 1 <= x1 <= 4, 0 <= x2 <= 5, x3 >= 2
    r = 10
    rez, p = broj_resenja([1, 0, 2], [4, 5, r], r)
    print("Koeficijenti proizvoda do x^10:", p)
    print("Broj resenja jednacine:", rez)
    brute = sum(1 for x1 in range(1, 5) for x2 in range(0, 6)
                if r - x1 - x2 >= 2)
    formula = comb(9, 2) - comb(5, 2) - comb(3, 2)
    assert rez == brute == formula == 23
    print("Nabrajanjem:", brute, " formulom C(9,2) - C(5,2) - C(3,2):", formula)

    # Novcici: 6 po 1, 5 po 2 i 4 po 5 dinara, placamo 21 dinar
    # x2 mora biti parno, x3 deljivo sa 5, pa koristimo odgovarajuce polinome
    p = [1] + [0] * 21
    for koraci, maks in ((1, 6), (2, 5), (5, 4)):
        f = [0] * 22
        for e in range(maks + 1):
            f[koraci * e] = 1
        p = mnozi(p, f, 21)
    brute = sum(1 for a in range(7) for b in range(6) for c in range(5)
                if a + 2 * b + 5 * c == 21)
    assert p[21] == brute
    print("Placanje 21 dinara (6 x 1, 5 x 2, 4 x 5):", p[21], "nacina")
    print("Sve provere prosle. OK")
