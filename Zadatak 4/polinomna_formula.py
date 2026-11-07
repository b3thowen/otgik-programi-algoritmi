# Pokretanje: python3 polinomna_formula.py [n] [l]
from math import factorial


def binomni(n, m):
    if m < 0 or m > n:
        return 0
    if m > n - m:
        m = n - m
    r = 1
    for j in range(1, m + 1):
        r = r * (n - m + j) // j
    return r


def polinomni_koef(n, ms):
    """C(n; m1,...,ml) = n! / (m1! ... ml!)  (Teorema 4: proizvod binomnih koef.)"""
    assert sum(ms) == n
    r, ostalo = 1, n
    for m in ms:
        r *= binomni(ostalo, m)
        ostalo -= m
    return r


def razvoj(n, l):
    """Vraca listu (koef, (m1,...,ml)) za sve vektore sa zbirom n.
    Rekurzivno: za poziciju i biramo m_i od 'preostalo' do 0; poslednji je odredjen."""
    rezultat = []
    m = [0] * l

    def rekurzija(i, preostalo, koef):
        if i == l - 1:
            m[i] = preostalo
            rezultat.append((koef, tuple(m)))
            return
        for t in range(preostalo, -1, -1):
            m[i] = t
            rekurzija(i + 1, preostalo - t, koef * binomni(preostalo, t))

    rekurzija(0, n, 1)
    return rezultat


def u_tekst(koef, ms, imena):
    delovi = []
    for ime, e in zip(imena, ms):
        if e == 1:
            delovi.append(ime)
        elif e > 1:
            delovi.append(f"{ime}^{e}")
    s = "".join(delovi)
    if koef != 1 or not s:
        s = str(koef) + s
    return s


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    l = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    imena = ["x", "y", "z", "w", "u", "v"][:l] if l <= 6 else [f"x{i+1}" for i in range(l)]
    r = razvoj(n, l)
    print(f"(" + " + ".join(imena) + f")^{n} = " + " + ".join(u_tekst(k, ms, imena) for k, ms in r))
    print()
    print("Broj sabiraka:", len(r), "| C(n+l-1, l-1) =", binomni(n + l - 1, l - 1))
    print("Zbir koeficijenata:", sum(k for k, _ in r), "| l^n =", l ** n)
    assert len(r) == binomni(n + l - 1, l - 1)
    assert sum(k for k, _ in r) == l ** n
    for k, ms in r:
        assert k == factorial(n) // __import__("math").prod(factorial(t) for t in ms)
    print("Provera preko formule n!/(m1!...ml!): OK")
    print("Primer 11: C(9; 3,2,4) =", polinomni_koef(9, [3, 2, 4]))
    print("Primer 7 (MATEMATIKA): C(10; 2,3,2,1,1,1) =", polinomni_koef(10, [2, 3, 2, 1, 1, 1]))
