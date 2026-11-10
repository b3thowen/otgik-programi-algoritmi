# Zadatak 5 - homogena relacija drugog reda a[n] = c1*a[n-1] + c2*a[n-2]
from math import sqrt, acos, cos, sin
from niz_iteracijom import niz_iteracijom


def resi_red_dva(c1, c2, a0, a1, n):
    """Vraca a[n] po formuli dobijenoj iz karakteristicne jednacine (c2 != 0)."""
    D = c1 * c1 + 4 * c2
    if D > 0:
        x1 = (c1 + sqrt(D)) / 2
        x2 = (c1 - sqrt(D)) / 2
        alfa1 = (a1 - a0 * x2) / (x1 - x2)
        alfa2 = a0 - alfa1
        return alfa1 * x1 ** n + alfa2 * x2 ** n
    if D == 0:
        x = c1 / 2
        alfa = a0
        beta = a1 / x - a0
        return (alfa + beta * n) * x ** n
    ro = sqrt(-c2)
    teta = acos(c1 / (2 * ro))
    A = a0
    B = (a1 / ro - A * cos(teta)) / sin(teta)
    return ro ** n * (A * cos(n * teta) + B * sin(n * teta))


def provera(c1, c2, a0, a1, N=20, eps=1e-6):
    a = niz_iteracijom(2, [0, c1, c2], [a0, a1], N)
    return all(abs(a[n] - resi_red_dva(c1, c2, a0, a1, n)) <= eps * max(1, abs(a[n]))
               for n in range(N + 1))


if __name__ == "__main__":
    primeri = [
        ("Primer 8, Fibonaci", 1, 1, 0, 1),
        ("Primer 9, razliciti koreni", 1, 2, 2, 7),
        ("Primer 10, dvostruki koren", 4, -4, 2, 1),
        ("Primer 13, kompleksni koreni", 2, -2, 1, 3),
    ]
    for ime, c1, c2, a0, a1 in primeri:
        vr = [round(resi_red_dva(c1, c2, a0, a1, n), 6) for n in range(6)]
        ok = provera(c1, c2, a0, a1)
        print(f"{ime}: {vr}  poklapa se sa iteracijom: {ok}")
        assert ok
    print("Sve provere prosle. OK")
