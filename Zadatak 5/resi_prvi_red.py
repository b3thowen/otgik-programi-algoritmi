# Zadatak 5 - nehomogena relacija prvog reda a[n] = c*a[n-1] + b*s^n, a[0] = a0
from niz_iteracijom import niz_iteracijom


def resi_prvi_red(c, b, s, a0, n):
    """Metoda jednakih koeficijenata (c != 0)."""
    if s != c:
        A = b * s / (s - c)
        alfa = a0 - A
        return alfa * c ** n + A * s ** n
    return (a0 + b * n) * c ** n


if __name__ == "__main__":
    primeri = [
        ("a(n) = 3a(n-1) + 2 na n, a(0) = 1", 3, 1, 2, 1),
        ("a(n) = 2a(n-1) + 2 na n, a(0) = 1 (s = c)", 2, 1, 2, 1),
        ("h(n) = 2h(n-1) + 3 na n, a(0) = 0", 2, 1, 3, 0),
    ]
    for ime, c, b, s, a0 in primeri:
        iter_ = niz_iteracijom(1, [0, c], [a0], 15, lambda n: b * s ** n)
        formula = [resi_prvi_red(c, b, s, a0, n) for n in range(16)]
        ok = all(abs(iter_[n] - formula[n]) < 1e-6 * max(1, abs(iter_[n])) for n in range(16))
        print(ime, "->", [round(x) for x in formula[:6]], "OK" if ok else "GRESKA")
        assert ok
    print("Sve provere prosle. OK")
