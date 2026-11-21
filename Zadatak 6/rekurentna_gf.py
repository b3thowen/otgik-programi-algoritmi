# Homogena linearna relacija drugog reda resena pomocu generatorne funkcije.
# a[n] = c1*a[n-1] + c2*a[n-2], c2 razlicito od 0, zadati a[0] i a[1].
import cmath
from stepeni_redovi import razvoj_racionalne, niz_iteracijom, lepo


def brojilac_imenilac(c1, c2, a0, a1):
    """A(x) = P(x)/Q(x), gde je Q(x) = 1 - c1*x - c2*x^2, P(x) = a0 + (a1 - c1*a0)x."""
    return [a0, a1 - c1 * a0], [1, -c1, -c2]


def opsti_clan(c1, c2, a0, a1, n):
    """Vrednost a[n] dobijena iz parcijalnih razlomaka funkcije A(x)."""
    D = c1 * c1 + 4 * c2
    if D != 0:
        l1 = (c1 + cmath.sqrt(D)) / 2
        l2 = (c1 - cmath.sqrt(D)) / 2
        alfa = (a1 - l2 * a0) / (l1 - l2)
        beta = a0 - alfa
        return (alfa * l1 ** n + beta * l2 ** n).real
    l = c1 / 2
    beta = a1 / l - a0
    return (a0 + beta * n) * l ** n


def resi(naziv, c1, c2, a0, a1, N=10):
    p, q = brojilac_imenilac(c1, c2, a0, a1)
    iz_reda = razvoj_racionalne(p, q, N)
    iteracija = niz_iteracijom([0, c1, c2], [a0, a1], N)
    formula = [opsti_clan(c1, c2, a0, a1, n) for n in range(N + 1)]
    print(naziv)
    print("  P(x) =", p, "  Q(x) =", q)
    print("  iz generatorne funkcije:", lepo(iz_reda)[:8])
    print("  iteracijom             :", iteracija[:8])
    ok = (list(iz_reda) == iteracija and
          all(abs(f - t) < 1e-6 for f, t in zip(formula, iteracija)))
    print("  formula se poklapa:", ok)
    return ok


if __name__ == "__main__":
    ok = True
    ok &= resi("a(n) = 5a(n-1) - 6a(n-2), a0 = 1, a1 = 4  (razliciti koreni)", 5, -6, 1, 4)
    ok &= resi("a(n) = 4a(n-1) - 4a(n-2), a0 = 2, a1 = 1  (dvostruki koren)", 4, -4, 2, 1)
    ok &= resi("a(n) = 2a(n-1) - 2a(n-2), a0 = 1, a1 = 3  (kompleksni koreni)", 2, -2, 1, 3)
    ok &= resi("Fibonaci: a(n) = a(n-1) + a(n-2), a0 = 0, a1 = 1", 1, 1, 0, 1)
    print("Sve provere prosle. OK" if ok else "Ima neslaganja!")
