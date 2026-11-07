# Pokretanje: python3 binomna_formula.py [n]

def binomni(n, m):
    """C(n, m) mnozenjem i deljenjem (bez velikih faktorijela)."""
    if m < 0 or m > n:
        return 0
    if m > n - m:
        m = n - m
    r = 1
    for j in range(1, m + 1):
        r = r * (n - m + j) // j # posle j-tog koraka r = C(n-m+j, j)
    return r


def stepen(ime, e):
    if e == 0:
        return ""
    return ime if e == 1 else f"{ime}^{e}"


def razvoj_binoma(n, a="x", b="y"):
    """Ispisuje (a + b)^n u razvijenom obliku koristeci C(n,m+1) = C(n,m)*(n-m)/(m+1)."""
    c = 1
    sabirci = []
    for m in range(n + 1):
        s = (str(c) if c != 1 else "") + stepen(a, n - m) + stepen(b, m)
        sabirci.append(s if s else "1")
        c = c * (n - m) // (m + 1)
    return " + ".join(sabirci)


def vrednost_binoma(n, x, y):
    """Za brojeve x i y: sabira C(n,m) * x^(n-m) * y^m."""
    return sum(binomni(n, m) * x ** (n - m) * y ** m for m in range(n + 1))


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(f"(x + y)^{n} = {razvoj_binoma(n)}")
    print(f"(a + b)^4 = {razvoj_binoma(4, 'a', 'b')}")
    print("(x + 2)^5 za x = 1:", vrednost_binoma(5, 1, 2), "= 3^5 =", 3 ** 5)
    # provera: brojevna vrednost se poklapa sa direktnim stepenovanjem
    for nn in range(0, 12):
        assert vrednost_binoma(nn, 3, -2) == (3 + -2) ** nn
        assert vrednost_binoma(nn, 7, 5) == 12 ** nn
    print("Provera: zbir C(n,m)*x^(n-m)*y^m = (x+y)^n za brojeve. OK")
    print("Koeficijent uz x^3 y^4 u (2x - y)^7:", binomni(7, 3) * 2 ** 3 * (-1) ** 4)
