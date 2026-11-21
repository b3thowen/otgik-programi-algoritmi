# m-kombinacije multiskupa pomocu generatornih funkcija.
from itertools import product
from math import comb
from stepeni_redovi import mnozi, broj_resenja

if __name__ == "__main__":
    # Multiskup {2*a, 1*b, 3*c}: faktori (1+x+x^2), (1+x), (1+x+x^2+x^3)
    k = [2, 1, 3]
    p = [1]
    for ki in k:
        p = mnozi(p, [1] * (ki + 1), sum(k))
    print("Multiskup {2*a, 1*b, 3*c}, koeficijenti:", p)
    for m in range(sum(k) + 1):
        broj = sum(1 for t in product(*[range(ki + 1) for ki in k]) if sum(t) == m)
        assert broj == p[m]
    print("Broj 4-kombinacija:", p[4], " (provereno nabrajanjem)")

    # Neogranicen broj ponavljanja: 1/(1-x)^n, koeficijent C(n + m - 1, m)
    for n in (2, 3, 4):
        N = 10
        p = [1] + [0] * N
        for _ in range(n):
            p = mnozi(p, [1] * (N + 1), N)
        assert p == [comb(n + m - 1, m) for m in range(N + 1)]
    print("Neogranicena ponavljanja: koeficijenti su C(n + m - 1, m), n = 2, 3, 4. OK")

    # Kutija: 30 crvenih, 40 plavih, 50 belih lopti, biramo 70
    rez, _ = broj_resenja([0, 0, 0], [30, 40, 50], 70)
    brute = sum(1 for i in range(31) for j in range(41) if 0 <= 70 - i - j <= 50)
    assert rez == brute == 1061
    print("Lopte (30, 40, 50), izbor 70 lopti:", rez)
    print("Formulom C(72,2) - C(41,2) - C(31,2) - C(21,2) =",
          comb(72, 2) - comb(41, 2) - comb(31, 2) - comb(21, 2))
    print("Sve provere prosle. OK")
