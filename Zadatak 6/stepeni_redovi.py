# Pomocne funkcije za rad sa stepenim redovima (skracenim do stepena N).
# Svi ostali programi uvoze ovaj fajl, pa treba da budu u istom folderu.
from fractions import Fraction


def mnozi(a, b, N):
    """Proizvod dva stepena reda, zadrzava clanove do stepena N."""
    c = [0] * (N + 1)
    for i in range(min(len(a), N + 1)):
        if a[i] == 0:
            continue
        for j in range(min(len(b), N + 1 - i)):
            c[i + j] += a[i] * b[j]
    return c


def razvoj_racionalne(p, q, N):
    """Koeficijenti reda P(x)/Q(x) do stepena N, uz q[0] razlicito od 0.

    Iz b * Q = P sledi q0*b[n] = p[n] - zbir q[i]*b[n-i], i = 1..min(n, k).
    """
    b = []
    for n in range(N + 1):
        s = Fraction(p[n]) if n < len(p) else Fraction(0)
        for i in range(1, min(n, len(q) - 1) + 1):
            s -= q[i] * b[n - i]
        b.append(s / q[0])
    return b


def binom_uopsteni(alfa, k):
    """Uopsteni binomni koeficijent C(alfa, k) za realno (racionalno) alfa."""
    r = Fraction(1)
    for i in range(k):
        r = r * (Fraction(alfa) - i) / (i + 1)
    return r


def binomni_red(alfa, N):
    """Koeficijenti reda (1 + x)^alfa do stepena N."""
    return [binom_uopsteni(alfa, k) for k in range(N + 1)]


def broj_resenja(donje, gornje, r):
    """Broj resenja jednacine x1 + ... + xn = r uz donje[i] <= xi <= gornje[i].

    Za svaku promenljivu uzimamo polinom x^donje + ... + x^gornje, mnozimo ih
    (skraceno do stepena r) i citamo koeficijent uz x^r.
    """
    proizvod = [1] + [0] * r
    for lo, hi in zip(donje, gornje):
        hi = min(hi, r)
        faktor = [0] * (r + 1)
        for e in range(lo, hi + 1):
            faktor[e] = 1
        proizvod = mnozi(proizvod, faktor, r)
    return proizvod[r], proizvod


def niz_iteracijom(c, a0, N):
    """Clanovi a[0..N] homogene relacije a[n] = c[1]a[n-1] + ... + c[k]a[n-k]."""
    k = len(c) - 1
    a = list(a0)
    for n in range(k, N + 1):
        a.append(sum(c[i] * a[n - i] for i in range(1, k + 1)))
    return a


def lepo(lista):
    """Razlomke ciji je imenilac 1 prikazuje kao cele brojeve."""
    return [int(x) if Fraction(x).denominator == 1 else str(Fraction(x))
            for x in lista]
